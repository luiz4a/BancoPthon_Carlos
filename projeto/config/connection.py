from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager 

# A URL de conexão para BD MySQL.
DATABASE_URL = f"mysql+pymysql://usuario:senha@host:porta"