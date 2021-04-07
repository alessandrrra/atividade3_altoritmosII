from veiculo import Veiculo

# Bicicleta
# num_marchas: int
# bagageiro: boolean
# + imprimir_informacoes(): void

class Bicicleta:
    def __init__(self, marca = None, qtd_rodas = None, modelo = None, num_marchas = None, bagageiro = None):
        Veiculo.__init__(self, marca, qtd_rodas, modelo)
        self.num_marchas = num_marchas
        self.bagageiro = bagageiro

    def imprimir_informacoes(self):
        Veiculo.imprimir_informacoes(self)
        #print("Número de marchas: ", self.num_marchas)
        #print("Bagageiro: ")
        if(self.bagageiro):
            print("Número de marchas: ", self.num_marchas, "\nBagageiro: Sim.")
        else:
            print("Número de marchas: ", self.num_marchas, "\nBagageiro: Não.")