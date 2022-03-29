from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create a sqlite engine instance
engine = create_engine("sqlite:///todo_list.db")

# Create a DeclarativeMeta instance
Base = declarative_base()