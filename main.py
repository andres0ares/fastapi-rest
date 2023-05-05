from fastapi import FastAPI
from datetime import datetime

app = FastAPI()


@app.get("/")
def read_root():
    return test()

def test():
    now = datetime.now()
    return now
