from automovel import Automovel

# Moto
# partida_eletrica: boolean
# + imprimir_informacoes(): void

class Moto:
    def __init__(self, marca = None, qtd_rodas = None, modelo = None, potencia_do_motor = None, partida_eletrica = None):
        Automovel.__init__(self, marca, qtd_rodas, modelo, potencia_do_motor)
        self.partida_eletrica = partida_eletrica

    def imprimir_informacoes(self):
        Automovel.imprimir_informacoes(self)
        if(self.partida_eletrica):
            print("Partida elétrica: Sim")
        else:
            print("Partida elétrica: Não")