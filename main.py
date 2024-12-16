import logging
import os

import openai
from fastapi import FastAPI
from fastapi.responses import JSONResponse

from src.llama_index import create_query_engine
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
def prompt(request_body: Request):
    try:
        engine = create_query_engine()

        result = engine.query(request_body.prompt)

        response = {
            "response": str(result),
            "metadata": result.metadata,
        }

        return response
    except Exception as e:
        return JSONResponse(status_code=404, content={"message": f"{e}"})
