# WAProject LLM Chatbot
![](/docs/waproject-llm-chatbot_ss.png)

This project is a FastAPI-based chatbot application utilizing LLMs (Large Language Models) via LangChain/LangGraph.

![](/docs/waproject-llm-chatbot_ss2.png)

<i>OBS: This was part of a job application process.</i>

## Features
- **LLM-powered Chatbot**: Utilizes LLMs to generate responses to user queries (Only `llama3-8b-8192` model for now).
- **Conversation History**: Stores the conversation history using Sqlite3, prioritizing simplicity for the app size.
- **Dockerized**: Builds a lightweight Docker image + `docker-compose.yml` with pluggable Groq API key.
- **Tightly packed**: Self-contained, lightweight, and easy to deploy and maintain by design.
- **Plain HTML/CSS/JS**: Minimal frontend using raw HTML/CSS/JS. Anything more complex would be overkill for this project.

## How to Run
- Copy `.env.example` to `.env` and fill in your groq api key: `cp .env.example .env`. <i>This step is required both locally and via docker compose.</i>

### Running locally
- Create a python virtual env and install the dependencies:
```bash
python3 -m venv .venv
source venv
pip install --upgrade pip setuptools
pip install -r requirements.txt
```
- Run the app with `python main.py`

### Running via docker compose
- Build the docker image: `docker build -t waproject-llm-chatbot .` (or run the `docker_build.sh` script)
- Docker compose time! `docker compose up` (Use `-d` at the end to run detached from your terminal).
- Open [localhost](http://localhost:8000) and have fun!

## Interest Points
- The application uses FastAPI and serves static files by itself (No S3, no CDN, no cloud).
- LangChain/LangGraph used for managing message sequences and data storage via SqliteSaver() at `.data/langchain.db`.
- The `.data/` directory volume is declared in the Dockerfile so it is managed by the Docker daemon itself.
- There is no user auth nor paralel conversations support, so the Langchain checkpoints's `thread_id` is hardcoded to `1`.
- [ShowdownJS](https://github.com/showdownjs/showdown) is used for markdown rendering from the LLMs responses.
- I could've used a vector database like Chroma or Pinecone, but given the time constraints I went with Sqlite3 for now.
- I added a few rules to play around with prompt engineering, so the LLM knows its name and don't disclose private or wrong information.
