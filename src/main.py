from fastapi import FastAPI

app = FastAPI(title="FastAPI Template")


@app.get("/")
def read_root():
    return {"message": "Hello World"}
