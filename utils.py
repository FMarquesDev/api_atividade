from models import Pessoas, Usuarios

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

def insere_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()

def consulta_todos_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)

if __name__ == '__main__':
    insere_usuario('Francisco', '1234')
    insere_usuario('Marques', '4321')
    consulta_todos_usuarios()
    #insere_pessoas()
    #altera_pessoas()
    #exclui_pessoas()
    #consulta_pessoas()
