from langchain_core.messages import HumanMessage
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, MessagesState, StateGraph


class LangchainApp:
    def __init__(self, model):
        self.model = model

        workflow = StateGraph(state_schema=MessagesState)
        workflow.add_edge(START, "model")
        workflow.add_node("model", self.call_model)
        memory = MemorySaver()
        self.app = workflow.compile(checkpointer=memory)

    def call_model(self, state: MessagesState) -> dict:
        response = self.model.invoke(state["messages"])
        return {"messages": response}

    def send_message(self, msg: str, thread_id: str) -> dict:
        config = {"configurable": {"thread_id": thread_id}}
        input_messages = [HumanMessage(msg)]
        return self.app.invoke({"messages": input_messages}, config=config)
