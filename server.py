import rpyc

class ServicoLista(rpyc.Service):
    def on_connect(self, conexao):
        self.lista = []

    def exposed_valor(self):
        return self.lista

    def exposed_adicionar(self, elemento):
        self.lista.append(elemento)
        return f"{elemento} adicionado com sucesso."

    def exposed_inserir(self, indice, elemento):
        if 0 <= indice <= len(self.lista):
            self.lista.insert(indice, elemento)
            return f"{elemento} inserido na posição {indice}."
        else:
            return "Índice inválido."

    def exposed_remover(self, elemento):
        try:
            self.lista.remove(elemento)
            return f"{elemento} removido com sucesso."
        except ValueError:
            return "Elemento não encontrado."

    def exposed_pesquisar(self, elemento):
        try:
            pos = self.lista.index(elemento)
            return f"{elemento} encontrado na posição {pos}."
        except ValueError:
            return "Elemento não encontrado."

    def exposed_ordenar(self):
        self.lista.sort()
        return "Lista ordenada com sucesso."

if __name__ == "__main__":
    from constRPYC import HOST, PORTA
    from rpyc.utils.server import ThreadedServer
    servidor = ThreadedServer(ServicoLista, port=PORTA, hostname=HOST)
    print(f"Servidor RPyC ativo em {HOST}:{PORTA}")
    servidor.start()
