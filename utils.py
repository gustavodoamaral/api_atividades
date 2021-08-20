from models import Pessoas


# INSERE dados na tabela pessoa
def insere_pessoas():
    pessoa = Pessoas(nome='Catarine', idade=34)
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

if __name__ == '__main__':
    #insere_pessoas()
    #altera_pessoas()
    exclui_pessoas()
    consulta_pessoas()
