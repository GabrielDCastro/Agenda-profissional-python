agenda={}

agenda['gabriel'] = {
    'telefone': '123456789',
    'email':'eu@gmail.com',
    'endereco': 'av. 1',}

agenda['nathalia'] = {
    'telefone': '123456999',
    'email':'ela@gmail.com',
    'endereco': 'av. 2',}

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

def incluir_contato(contato):
    telefone = input("Digite o telefone ")
    email = input("Digite  o email")
    endereco = input("Digite o endereço ")
    agenda[contato] = {
        'telefone': telefone,
        'email': email,
        'endereco': endereco
    }


def excluir_contato(contato):
    try:
        agenda.pop(contato)
    except:
        print("Contato inexistente")
def menu():
    print("1 - Mostrar agenda")
    print("2 - Buscar contato")
    print("3 - Incluir contato")
    print("4 - Editar contato")
    print("5 - Excluir contato")
    print("0 - fechar ")


while True:
    menu()
    opcao = int(input("Digite uma opção "))
    if opcao == 1:
        mostrar_contatos()
    if opcao == 2:
        contato=input("Digite o nome do contato")
        buscar_contato(contato)
    if opcao == 3:
        contato=input("Digite o nome do contato")
        try:
            agenda[contato]
            print("contato já existente ")
        except:
            incluir_contato(contato)
    if opcao == 4:
        contato=input("Digite o nome do contato")
        try:
            agenda[contato]
            incluir_contato(contato)
        except:
            print("Contato inexistente")
    if opcao==5:
        contato=input("Digite o nome do contato que deseja excluir")
        excluir_contato(contato)
    if opcao == 0:
        print("Fechando programa")
        break


