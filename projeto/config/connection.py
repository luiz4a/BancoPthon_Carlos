from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager 


# Parâmetros de conexão com MySQL.
db_user = "user"
db_passsword = "USer_password"
db_host = "localhost"
db_port = "3306"
db_name = "meu_banco"

# A URL de conexão para BD MySQL.
DATABASE_URL = f"mysql+pymysql://{db_user}:{db_passsword}@{db_host}:{db_port}/{db_name}"
