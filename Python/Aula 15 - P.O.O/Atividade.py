# FastPop
class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.saldo = 0
        self.avaliacao = 5
    
    def adicionarSaldo(self):
        valor = int(input('Digite o valor a ser adicionado:'))
        self.saldo += valor
        print(f'O valor de {valor} foi adicionado ao saldo do cliente {self.nome}')
    
    def removerSaldo(self):
        valor = int(input('Digite o valor a ser removido:'))
        self.saldo -= valor
        print(f'O valor de {valor} foi removido do saldo do cliente {self.nome}')

    def visualizarSaldo(self,valor):
        print(f'O saldo do cliente {self.nome} é de {self.saldo}')

cliente = Cliente('Alexandre' ,21)
cliente.adicionarSaldo()
cliente.removerSaldo()
print(cliente.saldo , cliente.avaliacao)