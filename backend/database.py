import os
import psycopg2


def get_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST", "factory-database"),
        database=os.getenv("DB_NAME", "factorydb"),
        user=os.getenv("DB_USER", "factoryuser"),
        password=os.getenv("DB_PASSWORD", "factorypass"),
        port=os.getenv("DB_PORT", "5432")
    )
