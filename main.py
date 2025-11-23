from fastapi import FastAPI

app = FastAPI()

@app.get("/main")
def read_main():
    return {"message": "ya chto pohozh na abonenta"}
