import os
from typing import List

from sqlalchemy import URL, Engine, create_engine, text


def get_sql_engine() -> Engine:
    database_url = URL.create(
        drivername="postgresql",
        username=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        database=os.getenv("POSTGRES_DB"),
    )
    return create_engine(database_url)

def get_table_names(engine: Engine, schema: str = "public") -> List[str]:
    query = text("""
        SELECT tablename 
        FROM pg_catalog.pg_tables 
        WHERE schemaname = :schema;
    """)
    with engine.connect() as connection:
        return connection.execute(query, {"schema": schema}).scalars().all()
