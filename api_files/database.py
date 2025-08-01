from sqlalchemy.orm import *
from sqlalchemy import create_engine

Url = "postgresql+psycopg2://postgres:admin@localhost:5432/To_do_API"

engine = create_engine(Url)

SessionLocal = sessionmaker(bind=engine,autoflush=False, autocommit=False)

Base = declarative_base()

def run_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

