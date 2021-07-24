from fastapi import FastAPI

new_app = FastAPI()

html = ""
with open('index.html', 'r') as f:
    html = f.read()

@new_app.get("/")
async def get():
    return HTMLResponse(html)
