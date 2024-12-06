from pydantic import BaseModel


class Request(BaseModel):
    prompt: str


class Response(BaseModel):
    message: str


class Message(BaseModel):
    message: str
