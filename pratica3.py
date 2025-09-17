def cadastro():
    nome= input("\n digite seu nome: ")
    cpf= input ("\n digite seu cpf: ")
    endereco= input("\n digite seu endereço: ")
    idade=  int(input("\n digite sua idade: "))
    
    print("\n Cadastro de Usuario")
    print("seu endereço é ", endereco)
    print("seu nome é ", cpf)
    print("seu nome é ", nome)

    if idade < 18:
        print("voce é menor de idade, não pode se cadastrar")
    else:
        print("voce pode se cadastrar.")

cadastro()