import os

from langchain_core.messages import HumanMessage, RemoveMessage
from langgraph.graph import START, MessagesState, StateGraph
from langgraph.checkpoint.sqlite import SqliteSaver
import sqlite3


class LangchainApp:
    def __init__(self, model):
        self.model = model

        workflow = StateGraph(state_schema=MessagesState)
        workflow.add_edge(START, "model")
        workflow.add_node("model", self.call_model)
        if not os.path.exists(".data"):
            os.makedirs(".data")
        self.conn = sqlite3.connect(".data/langchain.db", check_same_thread=False)
        self.memory = SqliteSaver(self.conn)
        self.app = workflow.compile(checkpointer=self.memory)

    def call_model(self, state: MessagesState) -> dict:
        response = self.model.invoke(state["messages"])
        return {"messages": response}

    def send_message(self, msg: str, thread_id: str) -> dict:
        config = {"configurable": {"thread_id": thread_id}}
        input_messages = [HumanMessage(msg)]
        return self.app.invoke({"messages": input_messages}, config=config)

    def get_chat_history(self, thread_id: str):
        config = {"configurable": {"thread_id": thread_id}}
        messages = self.app.get_state(config).values.get('messages') or []
        return messages

    def delete_messages(self, thread_id: str):
        config = {"configurable": {"thread_id": thread_id}}
        messages = self.app.get_state(config).values["messages"]
        remove_calls = [RemoveMessage(id=m.id) for m in messages]
        self.app.update_state(config, {"messages": remove_calls})
