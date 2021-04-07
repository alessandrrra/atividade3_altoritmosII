from veiculo import Veiculo

# Automóvel
# potencia_do_motor: double
# + imprimir_informacoes(): void

class Automovel(Veiculo):
    def __init__(self, marca = None, qtd_rodas = None, modelo = None, potencia_do_motor = None):
        Veiculo.__init__(self, marca, qtd_rodas, modelo)
        self.potencia_do_motor = potencia_do_motor

    def imprimir_informacoes(self):
        Veiculo.imprimir_informacoes(self)
        print("Potência do motor: ", self.potencia_do_motor)