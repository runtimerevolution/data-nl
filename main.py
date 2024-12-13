import logging
import os

import openai
from fastapi import FastAPI
from fastapi.responses import JSONResponse

from src.database_retriever import query_engine
from src.schemas import Message, Request, Response

logging.basicConfig(level=logging.INFO)

API_TITLE = os.getenv("API_TITLE", "Project")

app = FastAPI(title=API_TITLE, docs_url="/")

openai.api_key = os.getenv("OPENAI_API_KEY")


@app.post(
    "/prompt",
    status_code=201,
    response_model=Response,
    responses={404: {"model": Message}},
)
async def prompt(request_body: Request):
    try:
        return {"message": query_engine().query(request_body.prompt).__str__()}
    except Exception as e:
        return JSONResponse(status_code=404, content={"message": f"{e}"})
