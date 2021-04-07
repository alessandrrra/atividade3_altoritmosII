'''
Implementar as classes do diagrama a seguir:
Crie o construtor para cada uma das classes
O método acelerar da classe Veículo deve somar o valor passado por parâmetro da velocidadeAtual do veículo.
O método frear da classe Veículo deve subtrair o valor passado por parâmetro da velocidadeAtual do veículo.
O método imprimir_informacoes de cada uma das classes deve exibir na tela o conteúdo de cada um dos atributos da classe.
'''

# Veículo
# marca: string
# qtd_rodas: int
# modelo: string
# velocidade: int = 0
# + imprimir_informacoes(): void
# + acelerar(valor: int): void
# + frear(valor: int): void

# Bicicleta
# num_marchas: int
# bagageiro: boolean
# + imprimir_informacoes(): void

# Automóvel
# potencia_do_motor: double
# + imprimir_informacoes(): void

# Moto
# partida_eletrica: boolean
# + imprimir_informacoes(): void

# Carro
# qtd_portas: int
# + imprimir_informacoes(): void

from veiculo import Veiculo
from automovel import Automovel
from moto import Moto
from carro import Carro
from bicicleta import Bicicleta

divisao = "--------------------"

veiculo = Veiculo("Volkswagen", 4, "Jetta")
veiculo.imprimir_informacoes()
print(divisao)

automovel = Automovel("Volkswagen", 4, "Jetta", 2.0)
automovel.imprimir_informacoes()
print(divisao)

moto = Moto("BMW", 2, "R 1250 GS", 1.5, True)
moto.imprimir_informacoes()
moto.acelerar(100)
print(divisao)

carro = Carro("Volkswagen", 4, "Jetta", 2.0, 4)
carro.imprimir_informacoes()
carro.acelerar(80)
carro.frear(20)
print(divisao)

bicicleta = Bicicleta("Caloi", 0, "Vulcan", 27, True)
bicicleta.imprimir_informacoes()
bicicleta.acelerar(30)
frear(15)
