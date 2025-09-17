def Escola():
    idade= int(input("\nQual é sua idade? "))

    if idade >= 18:
        print("\nVocê pode aceesar o site.")
    else:
        print("\nVocê é moner de idade, não pode acessar nosso site.")

    nome= input("\nQual é seu nome?")

    #endereco= input("\nQual é seu endereço?")
    
    fun= int(input("\nDigite 1 para aluno, 2 para professor, 3 para diretor, 4 para coordenador: "))
    if fun== 1:
        print("\nVocê entrou como aluno.")

    if fun== 2:
        print("\nVocê entrou como professor.")
    N= int(input("\nA nota do aluno é? "))
    av= int(input("\nDigite 1 para lançar nota, 2 para lançar avaliação: "))

    if av== 1:
        print("A nota lançada para o aluno",nome,"e a nota dele é",N)

    opc= int(input("\nDigite 1 para consultar nota, 2 para consultar avaliações, 3 para sair: "))
    if opc == 1:
        print("\nSua nota é",N)
    if opc== 2:
        print("\nSua avaliação sera dia 04/08/2100")
    if opc== 3:
        print("Sair.")
    
    if av== 2:
        opc2= int(input("\nQuando será feita a avaliação? "))
        print("A avaliação será aplicada no dia ",opc2)
        print("sair.")

    if fun==3:
        print("\nVocê entrou como Diretor.")
        N1= int(input("\nDigite 1 para Gestão Administrativa, 2 para Gestão pedagogica, 3 para projetos e 4 para disciplina: "))

        if N1== 1:
            print("Você agora estar em gestão administrativa.")
             


 
Escola()
    