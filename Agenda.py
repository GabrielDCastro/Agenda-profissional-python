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
    print("Nome:", contato)
    print("Telefone:", agenda[contato]['telefone'])
    print("Email:", agenda[contato]['email'])
    print("Endereço:", agenda[contato]['endereco'])

mostrar_contatos()
buscar_contato('gabriel')

