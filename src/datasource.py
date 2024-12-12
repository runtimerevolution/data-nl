import os
from typing import List

from llama_index.core import Document, VectorStoreIndex
from llama_index.core.base.base_query_engine import BaseQueryEngine
from llama_index.readers.database import DatabaseReader

READER = DatabaseReader(
    uri=os.getenv("DATABASE_URI", "postgresql://postgres:postgres@db:5432/postgres"),
    # scheme=os.getenv("DATABASE_SCHEMA", "postgres"),
    # host=os.getenv("DATABASE_HOST", "localhost"),
    # port=os.getenv("DATABASE_PORT", "5432"),
    # user=os.getenv("DATABASE_USER", "postgres"),
    # password=os.getenv("DATABASE_PASSWORD", "postgres"),
    # dbname=os.getenv("DATABASE_NAME", "postgres"),
)


def load_documents(prompt: str) -> List[Document]:
    sql_query = "SELECT * FROM rainfall"
    return READER.load_data(query=sql_query)


def vectorize_documents(documents: List[Document]) -> VectorStoreIndex:
    print(f"{documents=}")
    return VectorStoreIndex.from_documents(documents)


def get_query_engine(index: VectorStoreIndex) -> BaseQueryEngine:
    return index.as_query_engine()
