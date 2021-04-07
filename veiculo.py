# Veículo
# marca: string
# qtd_rodas: int
# modelo: string
# velocidade: int = 0
# + imprimir_informacoes(): void
# + acelerar(valor: int): void
# + frear(valor: int): void

class Veiculo:
    def __init__(self, marca = None, qtd_rodas = None, modelo = None):
        self.marca = marca
        self.qtd_rodas = qtd_rodas
        self.modelo = modelo
        self.velocidade = 0

    def imprimir_informacoes(self):
        print("Marca: ", self.marca)
        print("Quantidade de rodas: ", self.qtd_rodas)
        print("Modelo: ",self.modelo)
        print("Velocidade: ", self.velocidade)

    def acelerar(self, valor):
        self.velocidade = self.velocidade + valor
        print("Velocidade atual: ", self.velocidade)

    def frear(self, valor):
        self.velocidade = self.velocidade - valor
        if(self.velocidade < 0):
            self.velocidade = 0
        print("Velocidade atual: ", self.velocidade)