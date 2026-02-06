from fastapi import FastAPI



app = FastAPI()


@app.get("/")
def index():
    return "hello md atik hasan"


@app.get("/about")
def about():
    return "this is about section"