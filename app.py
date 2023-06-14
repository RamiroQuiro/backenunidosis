from fastapi import FastAPI
from router.user import user
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI()


origins=[
    'http://localhost:8000',
    'http://localhost:3000',
    'http://172.16.3.94:3000',
    'http://172.16.3.94:8000',
    'http://localhost:3000/dashboard'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(user)
@app.get('/')
def helloword():
    return "Ramiro Quiroga DeveloperWeb | Sistema Unidosis Backend | FastAPI"