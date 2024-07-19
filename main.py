from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import firebase_admin
from firebase_admin import credentials, firestore
# from fastapi.middleware.cors import CORSMiddleware
from dotenv import dotenv_values

config = dotenv_values(".env")

cred = credentials.Certificate(config)
firebase_admin.initialize_app(cred)

db = firestore.client()
app = FastAPI(title="User", version="1.0.0")

# origins = [
#     "http://localhost.tiangolo.com",
#     "https://localhost.tiangolo.com",
#     "http://localhost",
#     "http://localhost:8080",
# ]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )


@app.post("/add_users")
async def add_user(dynamicUser: BaseModel, request: Request):
    try:
        user_data = await request.json()
        doc_ref = db.collection('users').document()
        if doc_ref:
            user_data['user_id'] = doc_ref.id
            doc_ref.set(user_data)
            return JSONResponse(content={"statusCode": 201, "statusMessage": "User Created", "data": user_data})
    except Exception as E:
        return JSONResponse(content={"statusCode": None, "statusMessage": f"{E}", "data": None})


@app.get("/get_users")
async def get_users():
    try:
        users = []
        docs = db.collection('users').stream()
        if docs:
            for doc in docs:
                users.append(doc.to_dict())
            return JSONResponse(content={"statusCode": 200, "statusMessage": "OK", "data": users})
    except Exception as E:
        return JSONResponse(content={"statusCode": None, "statusMessage": f"{E}", "data": None})


@app.patch("/update_users/{user_id}")
async def update_user(user_id: str, dynamicUser: BaseModel, request: Request):
    try:
        user_data = await request.json()
        doc_ref = db.collection('users').document(user_id)
        if doc_ref:
            doc_ref.update(user_data)
            return JSONResponse(content={"statusCode": 200, "statusMessage": "User Updated", "data": doc_ref.get().to_dict()})
    except Exception as E:
        return JSONResponse(content={"statusCode": None, "statusMessage": f"{E}", "data": None})


@app.delete("/delete_users/{user_id}")
async def delete_user(user_id: str):
    try:
        doc_ref = db.collection('users').document(user_id)
        if doc_ref:
            doc_ref.delete()
            return JSONResponse(content={"statusCode": 200, "statusMessage": "User Deleted", "data": None})
    except Exception as E:
        return JSONResponse(content={"statusCode": None, "statusMessage": f"{E}", "data": None})
