from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, Session, sessionmaker

Base = declarative_base()

def connect_to_database(client, password, host, db):
    try:
        postgresql_url = "postgresql://{}:{}@{}/{}".format(
            client, password, host, db)
        engine = create_engine(postgresql_url)
        Base.metadata.create_all(bind=engine)
        return engine, sessionmaker(autocommit=False, autoflush=False, bind=engine)
    except Exception as e:
        print("Error connecting to database:", str(e))
        return None
    
def init_db():
    engine_session = connect_to_database('client', 'password', 'localhost:5432', 'weatherman')
    return engine_session
