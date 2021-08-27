from models import Pessoas, Usuarios


# INSERE dados na tabela pessoa
def insere_pessoas():
    pessoa = Pessoas(nome='gustavo', idade=24)
    print(pessoa)
    pessoa.save()


# Realiza CONSULTA na tabela pessoa
def consulta_pessoas():
    pessoas = Pessoas.query.all()
    print(pessoas)
    pessoa = Pessoas.query.filter_by(nome='Juliana').first()
    print(pessoa.idade)


# ALTERA dados na tabela pessoa
def altera_pessoas():
    pessoa = Pessoas.query.filter_by(nome='Luca').first()
    pessoa.nome = 'Bruno'
    pessoa.save()


# EXCLUI dado na tabela pessoa
def exclui_pessoas():
    pessoa = Pessoas.query.filter_by(nome='Bruno').first()
    pessoa.delete()

def insere_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()

def consulta_todos_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)

if __name__ == '__main__':
    #insere_usuario('gustavo', "1234")
    #insere_usuario("fernanda", "5678")
    consulta_todos_usuarios()
    #insere_pessoas()
    #altera_pessoas()
    #exclui_pessoas()
    #consulta_pessoas()
