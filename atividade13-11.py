class exploracao:
    def __init__(self, colonizar= None, ocupar= None):
        self.colonizar= colonizar
        self.ocupar= ocupar

    def executar(self) -> str:
        return f"\nO {self.colonizar} quer colonizar {self.ocupar}"

class iluminismo(exploracao):
    def __init__(self, pessoa = None, escolher = None):
        self.pessoa = pessoa
        self.escolher = escolher

    def executar(self):
        return f"\na {self.pessoa} Quer {self.escolher},"


class Pensamento(iluminismo):
    def __init__(self, pensar= None, imaginar= None):
        self.pensar= pensar
        self.imaginar= imaginar
    def executar(self):
        return f"Estou a {self.pensar} sobre mminha {self.imaginar}."

class Ideia(Pensamento):
    def __init__(self, viver= None, morrer= None, desisão= None):
        self.viver= viver
        self.morrer= morrer

    def executar(self):
        return f"Você quer."

print("Qual o nome do seu país")
pais = input();
print("Qual país voce quer colonizar?")
colonizar = input();
explorar = exploracao(pais, colonizar)

print("Qual o seu nome? ")
nome = input()
print("Gostaria de ser iluminado? 1 = sim 2 = não ");
escolha = input()

if escolha == 1:
    iluminacao = iluminismo(nome, "ser iluminada")
    print(escolha)
if escolha == 2:
    iluminacao = iluminismo(nome, "não ser iluminada")
    print(escolha)

print("O que voê quer pensar? ")
pensando = input()
print("O que você quer imaginar? ")
imaginando = input()
pensamento = Pensamento(pensando, imaginando)


decisão= int(input(("Digite 1 para viver ou 2 para morrer: ")))

if decisão == 1:
    ideia = Ideia("Viver")
    print(decisão)

if decisão == 2:
    ideia = Ideia("Morrer")
    print(decisão)

objetos = [explorar, iluminacao, pensamento, decisão]
for obj in objetos:
    print(obj.executar())
