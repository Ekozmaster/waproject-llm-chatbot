import fastapi


app = fastapi.FastAPI()
@app.get("/")
def hello():
    return {"message": "Hello World"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)