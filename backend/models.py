from sqlalchemy import Column, Integer, String, Float, JSON, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Movie(Base):
    __tablename__ = "movies"

    movies_id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, nullable=False)
    summary = Column(String, nullable=False)
    genres = Column(String, nullable=False)
    embedding = Column(JSON) 


DATABASE_URL = "sqlite:///./movies.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

def init_db():
    Base.metadata.create_all(bind=engine)
