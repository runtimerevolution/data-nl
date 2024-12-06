import logging
import os

from fastapi import FastAPI
from fastapi.responses import JSONResponse

from src.schemas import Message, Request, Response

logging.basicConfig(level=logging.INFO)


app = FastAPI(title=os.getenv("API_TITLE"), docs_url="/")


@app.post(
    "/prompt",
    status_code=201,
    response_model=Response,
    responses={404: {"model": Message}},
)
async def prompt(request_body: Request):
    try:
        return {"message": request_body.prompt}
    except Exception as e:
        return JSONResponse(status_code=404, content={"message": f"{e}"})
