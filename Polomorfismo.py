class exploração:
    def __init__(self, colonizar= None, ocupar= None):
        self.colonizar= colonizar
        self.ocupar= ocupar

    def expor(self) -> str:
        return f"\nA exploração estar querendo {self.colonizar}(colonizar sim/não) o mundo, estar {self.ocupar}"

class iluminismo:
    def __init__(self, iluninar= None, desilumizar= None):
        self.iluninar= iluninar
        self.desilumizar= desilumizar

    def executar(self):
        print("As pessoas estão {self.}")

def fazer_executar(obj):
    obj.executar()

#p = Pato
#h = pessoa

#fazer_quack(p)
#fazer_quack(h)


class Pensamento:
    def executar(self):
        print("Som gravado: quack quack!")

class Ideia:
    def executar(self):
        print("Eu gosto de viver minha vida")

objetos = [exploração(), iluminismo(), Pensamento(), Ideia()]
for obj in objetos:
    obj.executar()