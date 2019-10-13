agenda={}


def mostrar_contatos():
    for contato in agenda:
        buscar_contato(contato)
        print("------------------------------------")

def buscar_contato(contato):
    try:
        print("Nome:", contato)
        print("Telefone:", agenda[contato]['telefone'])
        print("Email:", agenda[contato]['email'])
        print("Endereço:", agenda[contato]['endereco'])
    except:
        print("Contato não existe")

def ler_detalhes_contato():
    telefone = input("Digite o telefone ")
    email = input("Digite  o email")
    endereco = input("Digite o endereço ")
    return telefone, email, endereco #além de retornar essa variáveis, retorna em formato de tupla

def incluir_contato(contato, telefone, email, endereco):
    agenda[contato] = {
        'telefone': telefone,
        'email': email,
        'endereco': endereco
    }
    salvar()


def excluir_contato(contato):
    try:
        agenda.pop(contato)
        salvar()
    except:
        print("Contato inexistente")

def exportar_contatos(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, 'w') as arquivo:
            for contato in agenda:
                telefone=agenda[contato]['telefone']
                email=agenda[contato]['email']
                endereco=agenda[contato]['endereco']
                arquivo.write("{},{},{},{}\n".format(contato,telefone,email,endereco))
        print("Agenda exportada com sucesso")
    except:
        print("Algum erro ocorreu")

def importar_contatos(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                detalhes= linha.strip().split(',')
                nome = detalhes[0]
                telefone = detalhes[1]
                email = detalhes[2]
                endereco = detalhes[3]
                incluir_contato(nome, telefone, email, endereco)
    except FileNotFoundError:
        print("Arquivo não encontrado")
    except Exception as error:
        print("Algum erro ocorreu")

def salvar():
    exportar_contatos('database.csv')

def carregar():
    try:
        with open('database.csv', 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                detalhes = linha.strip().split(',')
                nome = detalhes[0]
                telefone = detalhes[1]
                email = detalhes[2]
                endereco = detalhes[3]

                agenda[nome] = {
                    'telefone': telefone,
                    'email': email,
                    'endereco': endereco
                }
    except:
        print("Ocorreu algum erro")


def menu():
    print("1 - Mostrar agenda")
    print("2 - Buscar contato")
    print("3 - Incluir contato")
    print("4 - Editar contato")
    print("5 - Excluir contato")
    print("6 - Exportar contatos para arquivo de texto")
    print("7 - Importat contatos para arquivo de texto")
    print("0 - fechar ")

carregar()
while True:
    menu()
    opcao = input("Digite uma opção ")
    if opcao == '1':
        mostrar_contatos()
    if opcao == '2':
        contato=input("Digite o nome do contato")
        buscar_contato(contato)
    if opcao == '3':
        contato=input("Digite o nome do contato")
        try:
            agenda[contato]
            print("contato já existente ")
        except:
            telefone, email, endereco = ler_detalhes_contato()# leio cada variável e retorno em suas respectivas variáveis
            incluir_contato(contato, telefone, email, endereco)
    if opcao == '4':
        contato=input("Digite o nome do contato")
        try:
            agenda[contato]
            telefone, email, endereco = ler_detalhes_contato()  # leio cada variável e retorno em suas respectivas variáveis
            incluir_contato(contato, telefone, email, endereco)
        except:
            print("Contato inexistente")
    if opcao == '5':
        contato=input("Digite o nome do contato que deseja excluir")
        excluir_contato(contato)

    if opcao == '6':
        arquivo = input("Digite o nome do arquivo a ser Exportado")
        exportar_contatos(arquivo)


    if opcao == '7':
        arquivo=input("Digite o nome do arquivo a ser importado")
        importar_contatos(arquivo)

    if opcao == '0':
        print("Fechando programa")
        break



