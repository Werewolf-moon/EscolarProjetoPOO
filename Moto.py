class Moto:
    def __init__(self, marca, modelo, ano, cor, velocidade):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.velocidade = velocidade

    def acelerar(self, valor):
        self.velocidade += valor
        print(f"{self.modelo} acelerou para {self.velocidade} KM/H.")

    def frear(self, valor):
        self.velocidade -= valor
        print(f"{self.modelo} freiou para {self.velocidade} KM/H.")

    def detalhes(self):
        print(f"A marca da moto é {self.marca}. \nO modelo é {self.modelo}. \nO ano de fabricação é {self.ano}. "
              f"A cor do veículo é {self.cor}. \nSua velocidade é {self.velocidade} KM/H.")

moto1 = Moto("Kawasaki", "ninja", 1770, "azul", 56)
moto2 = Moto("Kawajima", "deck", 1556, "vermelho", 90)

if moto1.velocidade > moto2.velocidade:
    moto1.detalhes()
else:
    moto2.detalhes()
    print("The End.")