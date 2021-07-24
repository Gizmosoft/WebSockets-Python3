from fastapi import FastAPI
from string import ascii_letters
import random
from fastapi import File, UploadFile

app = FastAPI()
fake_storage = []

if __name__ == "__main__":
    uvicorn.run("test_fastapi:app", host="0.0.0.0", port=81, reload=True)

@app.get("/echo")
def echo():
    return "Hello Gealber!"

'''
@app.post("/register")
def register():
    id = generate_id()
    fake_storage.append({
        "id": id
    })
    return {"id": id}

def generate_id():
    return "".join(random.sample(ascii_letters, 10))

@app.post("/login")
def login(info: LoginInfo):
    id = info.id
    for user in fake_storage:
        if user["id"] == id:
            return "Ok, 200"
    return "403, Forbidden"

@app.post("/send")
async def send(file: UploadFile = File(...)):
    return {"filename": file.filename}
'''
