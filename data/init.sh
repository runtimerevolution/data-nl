#!/bin/bash
set -e

echo ">> Starting initialization with DATABASE_INIT_FILE=${DATABASE_INIT_FILE}"

if [[ "$DATABASE_INIT_FILE" == *.tar ]]; then
    echo ">> Detected tar backup: $DATABASE_INIT_FILE"
    pg_restore -U "$POSTGRES_USER" -d "$POSTGRES_DB" "/docker-entrypoint-initdb.d/$DATABASE_INIT_FILE"
    echo ">> Tar backup restored successfully."
elif [[ "$DATABASE_INIT_FILE" == *.sql ]]; then
    echo ">> Detected SQL file: $DATABASE_INIT_FILE"
    psql -U "$POSTGRES_USER" -d "$POSTGRES_DB" -f "/docker-entrypoint-initdb.d/$DATABASE_INIT_FILE"
    echo ">> SQL file executed successfully."
else
    echo ">> No valid .sql or .tar file specified for DATABASE_INIT_FILE."
fi

echo ">> Initialization completed successfully."