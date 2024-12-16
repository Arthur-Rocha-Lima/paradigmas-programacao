class Carro: 

    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def exibir_detalhes(self):
        print(self.marca)
        print(self.modelo)
        print(self.ano)

carro1 = Carro(marca="Toyota", modelo="Corolla", ano=2020)
carro2 = Carro(marca="Renault", modelo="Duster", ano=2024)

carro1.exibir_detalhes()