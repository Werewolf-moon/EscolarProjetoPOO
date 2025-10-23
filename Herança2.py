class Pessoa:
    def __init__(self= None, nome= None, cpf= None, disciplina= None):
        self.nome = nome
        self.cpf = cpf
        self.disciplina= disciplina

        def apresentar(self):
            base= super().apresentar()
            base= apresentar
            return f"Seu nome é {self.nome}, sua matricula é {self.matricula}, seu cpf é {self.cpf},"
        
        if nome is None:
            nome= input("\n2Qual é seu nome? ")
        if matricula is None:
            matricula= input("\n2Digite sua matricula: ")
        if cpf is None:
            cpf= input("\n2Digite seu CPF: ")


class Aluno(Pessoa):
    def __init__(self, nome= None, matricula= None, cpf= None):
        if nome is None:
            nome= input("\n1Qual é seu nome? ")
        if matricula is None:
            matricula= input("\n1Digite sua matricula: ")
        if cpf is None:
            cpf= input("\n1Digite seu CPF: ")
   
        super().__init__(nome, cpf)
        self.matricula = matricula

    def apresentar(self):
        base= super().apresentar() 
        return f"{base}, eu sou o aluno da EEP Onelio porto, minha matrícula é {self.matricula}."

class Professor(Aluno):
    def __init__(self, nome= None, cpf= None, matricula= None, disciplina= None):
        if nome is None:
            nome= input("\nDigite o nome de professor: ")
        if matricula is None:
            matricula= input("\nDigite sua matricula: ")
        if cpf is None:
            cpf= input("\nDigite seu CPF: ")
        if disciplina is None:
            disciplina= input("\nDigite a sua disciplina como professor: ")

        super().__init__(nome, cpf)
        super().__init__(matricula)
        super().__init__(disciplina)
        self.matricula = matricula

    def apresentar(self):
        base= super().apresentar() 
        return f"{base}, eu sou o professor da EEP Onelio porto, e minha matricula é {self.matricula}." 
        
# Progama principal
p= Pessoa()  
a= Aluno()
prof= Professor()

print(p.apresentar())
print(a.apresentar())
print(prof.apresentar())