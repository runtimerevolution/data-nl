from pydantic import BaseModel


class Request(BaseModel):
    prompt: str


class Response(BaseModel):
    response: str
    metadata: dict


class Message(BaseModel):
    message: str
