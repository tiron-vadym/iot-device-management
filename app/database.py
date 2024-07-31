import os

from dotenv import load_dotenv
from peewee import PostgresqlDatabase


load_dotenv()

db = PostgresqlDatabase(
    database=os.getenv("POSTGRES_DB"),
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD"),
    host=os.getenv("POSTGRES_HOST"),
    port=5432
)
