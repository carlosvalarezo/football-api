import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from adapters.orm import start_mappers

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DATABASE_PATH = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


start_mappers()
engine = create_engine(DATABASE_PATH)
get_session = sessionmaker(bind=engine)
