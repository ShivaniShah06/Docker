from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from dotenv import load_dotenv
import os

load_dotenv()
db_name = os.getenv("DB_NAME")
database_url = os.getenv("DATABASE_URL")

engine = create_engine(database_url,
                       echo=True
                       )
if database_exists(engine.url):
    print(f"Database {db_name} already exists")
if not database_exists(engine.url):
    create_database(engine.url)
    print("Database created!")

Base = declarative_base()

SessionLocal = sessionmaker(bind=engine)