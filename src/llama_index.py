from typing import List

from sqlalchemy import Engine

from llama_index.core import VectorStoreIndex
from llama_index.core.indices.struct_store.sql_query import (
    SQLTableRetrieverQueryEngine,
)
from llama_index.core.objects import ObjectIndex, SQLTableNodeMapping, SQLTableSchema
from llama_index.core.utilities.sql_wrapper import SQLDatabase
from src.utils import get_sql_engine, get_tables_names


def get_database_info(engine: Engine, table_list: List[str]):
    sql_database = SQLDatabase(engine, include_tables=table_list)

    table_node_mapping = SQLTableNodeMapping(sql_database)

    table_schemas = []
    for table_name in table_list:
        table_schemas.append(SQLTableSchema(table_name=table_name))

    return (
        sql_database,
        table_node_mapping,
        table_schemas,
    )


def vectorize_tables(
    table_schemas: List[SQLTableSchema], table_node_mapping: SQLTableNodeMapping
) -> ObjectIndex:
    return ObjectIndex.from_objects(
        table_schemas,
        table_node_mapping,
        VectorStoreIndex,
    )


def get_query_engine(
    sql_database: SQLDatabase, index: ObjectIndex
) -> SQLTableRetrieverQueryEngine:
    return SQLTableRetrieverQueryEngine(
        sql_database, index.as_retriever(similarity_top_k=1)
    )


def create_query_engine() -> SQLTableRetrieverQueryEngine:
    sql_engine = get_sql_engine()
    tables = get_tables_names(engine=sql_engine)

    sql_database, table_node_mapping, table_schemas = get_database_info(
        engine=sql_engine, table_list=tables
    )
    index = vectorize_tables(
        table_schemas=table_schemas, table_node_mapping=table_node_mapping
    )

    query_engine = get_query_engine(sql_database=sql_database, index=index)

    return query_engine
