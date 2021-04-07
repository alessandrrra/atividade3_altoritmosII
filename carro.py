from automovel import Automovel

# Carro
# qtd_portas: int
# + imprimir_informacoes(): void

class Carro:
    def __init__(self, marca = None, qtd_rodas = None, modelo = None, potencia_do_motor = None, qtd_portas = None):
        Automovel.__init__(self, marca, qtd_rodas, modelo, potencia_do_motor)
        self.qtd_portas = qtd_portas

    def imprimir_informacoes(self):
        Automovel.imprimir_informacoes(self)
        print("Quantidade de portas: ", self.qtd_portas)
