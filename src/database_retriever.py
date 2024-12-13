import os

import pandas as pd
from llama_index.core import SQLDatabase, VectorStoreIndex
from llama_index.core.indices.struct_store.sql_query import (
    SQLTableRetrieverQueryEngine,
)
from llama_index.core.objects import (
    ObjectIndex,
    SQLTableNodeMapping,
    SQLTableSchema,
)
from llama_index.llms.openai import OpenAI
from sqlalchemy import create_engine


def query_engine():
    OpenAI(temperature=0.1, model="gpt-4o")
    engine = create_engine(
        os.getenv("DATABASE_URI", "postgresql://postgres:postgres@db:5432/postgres")
    )

    df = pd.read_sql_query(
        "SELECT tablename FROM pg_catalog.pg_tables where schemaname='public';", engine
    )
    table_list = list(df["tablename"])

    sql_database = SQLDatabase(engine, include_tables=table_list)

    # set Logging to DEBUG for more detailed outputs
    table_node_mapping = SQLTableNodeMapping(sql_database)

    table_schema_objs = []
    for table_name in table_list:
        # add a SQLTableSchema for each table
        table_schema_objs.append(SQLTableSchema(table_name=table_name))

    obj_index = ObjectIndex.from_objects(
        table_schema_objs,
        table_node_mapping,
        VectorStoreIndex,
    )
    return SQLTableRetrieverQueryEngine(
        sql_database, obj_index.as_retriever(similarity_top_k=1)
    )
