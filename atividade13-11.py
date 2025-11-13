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
        return f"a {self.pessoa} Quer {self.escolher}"


class Pensamento:
    def __init__(self, pensar= None, imaginar= None, duvidar= None):
        self.pensar= pensar
        self.imaginar= imaginar
        self.duvidar= duvidar
    def executar(self):
        return f"Estou a {self.pensar} sobre mminha {self.imaginar}."

class Ideia:
    def __init__(self, viver= None, morrer= None):
        self.viver= viver
        self.morrer= morrer

    def executar(self):
        return f"Eu quero viver? {self.viver}. Eu quero morrer? {self.morrer}"

print("Qual o nome do seu país")
pais = input();
print("Qual país voce quer colonizar?")
colonizar = input();
explorar = exploracao(pais, colonizar)

print("Qual o seu nome?");
nome = input();
print("Gostaria de ser iluminado? 1 = sim 2 = não");
escolha = input();
if escolha == 1:
    iluminacao = iluminismo(nome, "ser iluminada")
if escolha == 2:
    iluminacao = iluminismo(nome, "não ser iluminada")

objetos = [explorar, iluminacao, Pensamento(), Ideia()]
for obj in objetos:
    print(obj.executar())
