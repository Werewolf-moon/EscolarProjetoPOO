class Casa:
    def __init__(self, tamanho=None, cor=None, quartos=None):
        self.tamanho = tamanho
        self.cor = cor
        self.quartos = quartos
    
    def descricao(self):
        self.cor= input("\nQual é a cor da sua casa? ")
        self.quartos= input("\nQuantos quartos a casa possui? ")
        self.tamanho= input("\nQual é o tamanho da casa em metros quadrados? ")
        return (f"\nCor: {self.cor}, \nNúmero de quartos: {self.quartos}, \nTamanho: {self.tamanho} m².")
        
cs = Casa()
print(cs.descricao())

class Pessoa:
    def __init__(self, __nome=None, __idade =None):
        self.__nome = __nome
        self.__idade = __idade 

    @property
    def nomear_pessoa(self):
        return self.__nome
    
    @nomear_pessoa.setter
    def nomear_pessoa(self, __nome):
        self.__nome = __nome
        self.__nome = input("\nQual é o seu nome? ")

    @property
    def idade_pessoa(self):
        return self.__idade

    @idade_pessoa.setter
    def idade_pessoa(self, __idade):
        self.__idade = __idade
        self.__idade = input("\nQual é a sua idade? ")

       
    def pensar(self, pensar= None):
        self.pensar = input("\nNo que você gostaria de pensar? ")
        return f"\nvocê está pensando em: {self.pensar}"
    
    def dançar(self, dançar=None):
        self.dançar = input("\nQue tipo de dança você gostaria de fazer? ")
        return f"\nEstá dançando: {self.dançar}"
    
    def cantar(self, cantar=None):
        self.cantar = input("\nVocê gostaria de cantar?(Digite o que quer cantar): ")
        return f"\nEstá cantando: {self.cantar}"
    
    def dormir(self, dormir=None):
        self.dormir = input("\nVocê quer dormir agora? (SIM ou NÃO): ")
        return f"\nStatus do sono de {self.__nome}; \ndormindo? {self.dormir}"
    
    def eu(self):
        return (f"\nNome é: {self.__nome}, \nPensamento atual é: {self.pensar}, \nDança preferida é: {self.dançar}, \nVocê Quer dormir? -> {self.dormir}.")
    
p = Pessoa()
print(p.cantar())
print(p.dançar())
print(p.pensar())
print(p.dormir())
print(p.eu())
