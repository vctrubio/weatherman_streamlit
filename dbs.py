import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, Session, sessionmaker

Base = declarative_base()

def connect_to_database(client, password, host, db):
    try:
        engine = create_engine('sqlite:///example.db')  # Use SQLite connection string
        Base.metadata.create_all(bind=engine)
        return sessionmaker(autocommit=False, autoflush=False, bind=engine)
    except Exception as e:
        raise Exception(f"Error connecting to database: {e}")

def init_db():
    return connect_to_database('client', 'password', 'localhost:5432', 'weatherman')
