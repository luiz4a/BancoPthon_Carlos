import os
from services.usuario_service import UsuarioService
from repositories.usuario_repository import UsuarioRepository
from config.connection import Session 


os.system("cls||clear")

def main():
    session = Session()
    repository = UsuarioService(session)
    service = UsuarioService(repository)


    # Criando um usuario 
    service.criar_usuario("Maria", "maria1@gmail.com", "123456")

    #Listando todos os usuarios.
    print(f"\nListando todos os usuarios.")
    lista_usuarios = service.listar_todos_usuarios()
    for usuario in lista_usuarios:
        print(f"{usuario.id} - {usuario.nome} - {usuario.email} - {usuario.senha}")

if __name__ == "__main__":
    main()  #Chamada para a função.
