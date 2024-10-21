from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base
from config.connection import db 

Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column (Integer, primary_key = True, autoincrement = True )
    nome = Column(String(150))
    email = Column(String(150), unique=True) #unique=True não aceita email ou dado repetido 
    senha = Column(String(150))


    def __init__(self, nome: str, email: str, senha: str):
        self.nome = nome 
        self.email = email 
        self.senha = senha 

#Criando Tabela no banco de dados.
Base.metadata.create_all(bind=db)