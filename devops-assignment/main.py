from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return { "message" : "Devops assignment by 0201AI221042"}