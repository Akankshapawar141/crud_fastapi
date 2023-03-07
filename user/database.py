from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import psycopg2

#conn_string = "host='localhost' dbname='postgresql' user='postgres' password='postgresql'"
#conn = psycopg2.connect(conn_string)
#SQLALCHEMY_DATABASE_URL = "sqlite:///./user.db"
SQLALCHEMY_DATABASE_URL ="postgresql://postgres:postgresql@localhost/postgres"
#('postgresql+psycopg2://user:password@hostname/database_name')

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)

Base = declarative_base()
