import fastapi

from llms.core import LangchainApp
from llms.groq import model


def main():
    langchain_app = LangchainApp(model=model)
    langchain_app.send_message(msg="Hi! I'm Bob", thread_id='1')
    second_msg = "Complete this phrase with my name: If 'x' had called the police, this would never have happened!"
    response = langchain_app.send_message(msg=second_msg, thread_id='1')
    response["messages"][-1].pretty_print()


app = fastapi.FastAPI()
@app.get("/")
def hello():
    return {"message": "Hello World"}


if __name__ == "__main__":
    import uvicorn
    # uvicorn.run(app, host="0.0.0.0", port=8000)
    main()
