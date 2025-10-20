import rpyc
from constRPYC import HOST, PORTA

conexao = rpyc.connect(HOST, PORTA)
remoto = conexao.root

print(remoto.adicionar("banana"))
print(remoto.adicionar("maçã"))
print(remoto.inserir(1, "laranja"))
print(remoto.valor())
print(remoto.pesquisar("maçã"))
print(remoto.remover("banana"))
print(remoto.ordenar())
print(remoto.valor())

conexao.close()
