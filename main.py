import fastapi
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from llms.core import LangchainApp
from llms.groq import model


langchain_app = LangchainApp(model=model)


app = fastapi.FastAPI()


class ChatMessage(BaseModel):
    messages: list


@app.post("/send-message/")
async def send_message(messages: ChatMessage):
    llm_response = langchain_app.send_message(msg=messages.messages[-1]['content'], thread_id='1')
    return {"messages": [{"sender": msg.type, "content": msg.content } for msg in llm_response["messages"]]}


# get endpoint to retrieve langchain messages to frontend
@app.get("/langchain-messages/")
async def get_langchain_messages():
    messages = langchain_app.get_chat_history('1')
    if not messages:
        return {"messages": []}
    return {"messages": [{"sender": msg.type, "content": msg.content} for msg in messages]}

app.mount("/", StaticFiles(directory="static", html=True), name="static")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
