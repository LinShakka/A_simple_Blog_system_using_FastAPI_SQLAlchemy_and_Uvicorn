from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"data":{"name":"Lin"}}

@app.get("/about")
def bout():
    return {"data":"about page"}