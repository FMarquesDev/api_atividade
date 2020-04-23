from models import Pessoas

# Insere dados na tabela pessoa
def insere_pessoas():
    pessoa = Pessoas(nome='Marques', idade=47)
    print(pessoa)
    pessoa.save()

# Realiza consulta na tabela pessoa
def consulta_pessoas():
    pessoas = Pessoas.query.all()
    print(pessoas)
    pessoa = Pessoas.query.filter_by(nome='Francisco').first()
    print(pessoa.idade)

# Altera dados na tabela pessoa
def altera_pessoas():
    pessoa = Pessoas.query.filter_by(nome='Marques').first()
    pessoa.nome = 'Fontenele'
    pessoa.save()

# Exclui dados na tabela pessoa
def exclui_pessoas():
    pessoa = Pessoas.query.filter_by(nome='Fontenele').first()
    pessoa.delete()

if __name__ == '__main__':
    #insere_pessoas()
    #altera_pessoas()
    exclui_pessoas()
    consulta_pessoas()
