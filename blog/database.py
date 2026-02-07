from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHAMY_DATABASE_URL = 'sqlite:///./blog.db'

engine = create_engine(SQLALCHAMY_DATABASE_URL, connect_arg={"check_same_thread": False})


SessionLocal  = sessionmaker(bind=engine, autocommit=False, autoflush=False)


Base = declarative_base()
