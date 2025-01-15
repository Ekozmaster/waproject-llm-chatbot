import fastapi
from fastapi.staticfiles import StaticFiles

# from llms.core import LangchainApp
# from llms.groq import model


# langchain_app = LangchainApp(model=model)


app = fastapi.FastAPI()
app.mount("/", StaticFiles(directory="static", html=True), name="static")


@app.get("/a")
def hello(message: str):
    # llm_response = langchain_app.send_message(msg=message, thread_id='1')
    # return {"messages": [{"sender": msg.type, "content": msg.content } for msg in llm_response["messages"]]}
    ...


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
