import os

from dotenv import load_dotenv
load_dotenv()


if not os.environ.get("GROQ_API_KEY"):
    raise RuntimeError("Couldn't find GROQ_API_KEY env var.")


from langchain_groq import ChatGroq

model = ChatGroq(model="llama3-8b-8192")
