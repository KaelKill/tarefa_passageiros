import os

def mostrar_menu() -> str:
    print("Opção 1: Cadastrar ou Editar o total de poltronas")
    print("Opção 2: Realizar reserva de poltrona")
    print("Opção 3: Visualizar poltronas disponíveis")
    print("Opção 4: Visualizar poltronas reservadas")
    print("Opção 5: Consultar passageiro pelo nome")
    print("Opção 6: Visualizar o total de poltronas reservadas e poltronas disponíveis")
    print("Opção 7: Sair do sistema.")
    return input('->  ')

def cadastrar_editar_poltronas():
    colunas =int(input("Digite o numero de colunas: "))
    linhas = int(input("Digite o numero de linhas: "))
    return [[0]*linhas for i in range(colunas)]
    

def reserva_de_poltronas(poltronas):
    os.system('cls')
    nome = input("Digite o nome para a reserva: ")
    coluna =int(input("Digite o numero de coluna: ")) - 1
    linha = int(input("Digite o numero de linha: ")) - 1

    p_col = len(poltronas[0])
    p_lin = len(poltronas)

    if(linha > p_lin or coluna > p_col):
        print("Seleção invalida")
        return poltronas
    
    if poltronas[linha][coluna] == 'disponivel':
        poltronas[linha][coluna] = nome
        print("Reserva realizada com sucesso")
    else:
        print("Assento indisponivel")

    return poltronas


def visualizar_poltronas_disponiveis(poltronas):
    p_col = len(poltronas[0])
    p_lin = len(poltronas)

    for i in range(p_lin):
        for j in range(p_col):
            if poltronas[i][j] == "disponivel":
                print("{}-{} disponivel".format(i + 1,j + 1))


def visualizar_poltronas_reservadas(poltronas):
    p_col = len(poltronas[0])
    p_lin = len(poltronas)

    for i in range(p_lin):
        for j in range(p_col):
            if poltronas[i][j] != "disponivel": 
                print("{}-{} disponivel".format(i + 1, j + 1))

def consultar_passageiro(poltronas):
    consulta = input("Nome do passageiro: ")
    
    p_col = len(poltronas[0])
    p_lin = len(poltronas)

    for i in range(p_lin):
        for j in range(p_col):
            if poltronas[i][j] == consulta: 
                print("Passageiro {} está alocado na poltrona {}-{}".format(consulta, i+1, j+1))
                return 


def mapa_de_poltronas(poltronas):
    p_col = len(poltronas[0])
    p_lin = len(poltronas)

    for i in range(p_col+ 1):
         print("{:2} |".format(i), end='')

    for i in range(p_lin):
        print("\r\n{:2} |".format(i + 1), end='')
        for j in range(p_col):
            print("{:2} |".format(' *' if poltronas[i][j] != "disponivel" else ' -'), end='')

    print('')
    print("Legenda:")
    print("*: Reservado")
    print("-: Disponivel")


def app():
    NUM_DE_COLUNAS = 10 
    NUM_DE_LINHAS = 30
    poltronas = [["disponivel"]*NUM_DE_COLUNAS for i in range(NUM_DE_LINHAS)]

    while(True):
        # os.system('cls')
        print('----------')
        selecao = mostrar_menu()

        if selecao == '1':
            poltronas = cadastrar_editar_poltronas()
        elif selecao == '2':
            poltronas = reserva_de_poltronas(poltronas)
        elif selecao == '3':
            visualizar_poltronas_disponiveis(poltronas)
        elif selecao == '4':
            visualizar_poltronas_reservadas(poltronas)
        elif selecao == '5':
            consultar_passageiro(poltronas)
        elif selecao == '6':
            mapa_de_poltronas(poltronas)
        elif selecao == '7':
            exit()
        else:
            print("Opçao invalida")



if __name__=="__main__":
    app()