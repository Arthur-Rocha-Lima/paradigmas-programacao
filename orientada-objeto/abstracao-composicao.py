from abc import ABC, abstractmethod

class FormaGeometrica(ABC):

    @abstractmethod
    def calcula_area(self):
        raise NotImplementedError("Este método deve ser implementado.")

class Circulo(FormaGeometrica):

    def __init__(self, raio):
        self.raio = raio

    def calcula_area(self):
        area = 3.14 * self.raio ** 2
        return area

class Retangulo(FormaGeometrica):

    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcula_area(self):
        return self.altura * self.largura

# circulo = Circulo(raio=10)

# area_circulo = circulo.calcula_area()
# print(area_circulo)

# retangulo = Retangulo(largura=10, altura=5)
# print(retangulo.calcula_area())

class Motor:

    def __init__(self, potencia):
        self.potencia = potencia
        self.ligado = False

    def ligar_motor(self):
        self.ligado = True

class Carro:

    def __init__(self, marca, modelo, motor):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor

    def exibir_detalhes(self):
        print(f"Carro {self.marca} {self.modelo}")

    def mostrar_potencia_motor(self):
        print(f"Motor de potencia: {self.motor.potencia} cavalos.")

motor = Motor(potencia=200)
motor.ligar_motor()
print(motor.potencia)
print(motor.ligado)

carro1 = Carro(marca="Honda", modelo="Civic", motor=motor)
carro1.exibir_detalhes()
carro1.mostrar_potencia_motor()