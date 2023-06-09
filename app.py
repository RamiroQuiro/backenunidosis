from fastapi import FastAPI
from router.user import user

app=FastAPI()

app.include_router(user)

@app.get('/')
def helloword():
    return "estamos con faztAPi"