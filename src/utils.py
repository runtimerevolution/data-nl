import os
from typing import List

import pandas as pd
from sqlalchemy import Engine, create_engine


def get_sql_engine() -> Engine:
    return create_engine(
        os.getenv("DATABASE_URI", "postgresql://postgres:postgres@db:5432/postgres")
    )


def get_tables_names(engine: Engine) -> List[str]:
    df = pd.read_sql_query(
        "SELECT tablename FROM pg_catalog.pg_tables where schemaname='public';", engine
    )
    return list(df["tablename"])
