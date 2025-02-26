class Pilha:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.itens = []

    def esta_vazia(self):
        return len(self.itens) == 0

    def esta_cheia(self):
        return len(self.itens) == self.capacidade

    def tamanho(self):
        return len(self.itens)

    def topo(self):
        if self.esta_vazia():
            raise IndexError("A pilha está vazia")
        return self.itens[-1]

    def push(self, item):
        if self.esta_cheia():
            raise OverflowError("A pilha está cheia")
        self.itens.append(item)

    def pop(self):
        if self.esta_vazia():
            raise IndexError("A pilha está vazia")
        return self.itens.pop()




