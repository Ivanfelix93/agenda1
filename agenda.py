AGENDA = {}


def mostra_contatos():
    if AGENDA:
        for contato in AGENDA:
            buscar_contato(contato)
            print('________________________')
    else:
        print('== Agenda vazia ==')


def buscar_contato(contato):
    try:
        print('Nome:', contato)
        print('Telefone:', AGENDA[contato]['telefone'])
        print('Email:', AGENDA[contato]['email'])
        print('Endereco:', AGENDA[contato]['endereco'])
    except KeyError:
        print('== Contato inexistente ==')
    except Exception as error:
        print('== Um erro inesperado ocorreu ==')
        print(error)

def ler_detalhes_contato():
    telefone = input('Digite o nome do telefone: ')
    email = input('Digite o nome do email: ')
    endereco = input('Digite o nome do endereco: ')
    return telefone, email, endereco


def incluir_editar_contato(contato, telefone, email, endereco):
    AGENDA[contato] = {
        'telefone': telefone,
        'email': email,
        'endereco': endereco,
    }
    salvar()
    print()
    print('== Contato {} adicionado/editado com sucesso =='.format(contato))
    print()


def excluir_contato(contato):
    try:
        AGENDA.pop(contato)
        salvar()
        print()
        print('== Contato {} excluido com sucesso =='.format(contato))
        print()
    except KeyError:
        print('== Contato inexistente ==')
    except Exception as error:
        print('== Um erro inesperado ocorreu ==')
        print(error)


def exporta_contatos(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, 'w') as arquivo:
            for contato in AGENDA:
                telefone = AGENDA[contato]['telefone']
                email = AGENDA[contato]['email']
                endereco = AGENDA[contato]['endereco']
                arquivo.write('{}.{}.{}.{}.\n'.format(contato, telefone, email, endereco))
        print('== Agenda exportada com sucesso ==')
    except Exception as error:
        print('== Algum erro aconteceu ==')
        print(error)

def importar_contatos(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                detalhes = linha.strip().split(',')

                nome = detalhes[0]
                telefone = detalhes[1]
                email = detalhes[2]
                endereco = detalhes[3]

                incluir_editar_contato(nome, telefone, email, endereco)
    except FileNotFoundError:
        print('== Arquivo não encontrado ==')
    except Exception as error:
        print('== Algum erro inesperado ocorreu ==')
        print(error)

def salvar():
    exporta_contatos('database.csv')


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

                AGENDA[nome] = {
                    'telefone': telefone,
                    'email': email,
                    'endereco': endereco,
                }
        print('== Database carregado com sucesso ==')
        print('== {} contatos carregados'.format(len(AGENDA)))
    except FileNotFoundError:
        print('== Arquivo não encontrado ==')
    except Exception as error:
        print('== Algum erro inesperado ocorreu ==')
        print(error)


def imprimir_menu():
    print('_____________________________________')
    print('1- Mostre todos os contatos da agenda')
    print('2- Buscar contatos')
    print('3- Incluir contatos')
    print('4- Editar contatos ')
    print('5- Excluir contatos')
    print('6- Esporta contatos csv')
    print('7- Importar contatos CSV')
    print('0- Fechar agenda')
    print('_____________________________________')

carregar()
while True:
    imprimir_menu()

    opcao = input(' Escolha uma opção: ')

    if opcao == '1':
        mostra_contatos()
    elif opcao == '2':
        contato = input(' Digite o nome do contato: ')
        buscar_contato(contato)
    elif opcao == '3':
        contato = input('Digite o nome do contato: ')

        try:
            AGENDA[contato]
            print('== Contato já existente ==')
        except KeyError:
            telefone, email, endereco = ler_detalhes_contato()
            incluir_editar_contato(contato, telefone, email, endereco)
    elif opcao == '4':
        contato = input('Digite o nome do contato: ')

        try:
            AGENDA[contato]
            print('== Contato já existente ==')
        except KeyError:
            telefone, email, endereco = ler_detalhes_contato()
            incluir_editar_contato(contato, telefone, email, endereco)
    elif opcao == '5':
        contato = input(' Digite o nome do contato: ')
        excluir_contato(contato)
    elif opcao == '6':
        exporta_contatos(nome_do_arquivo)
    elif opcao == '7':
        nome_do_arquivo = input('Digite o nome do arquivo a ser importado: ')
        importar_contatos(nome_do_arquivo)
    elif opcao == '0':
        print('== Fechar programa ==')
        break
    else:
        print('== Opção invalida ==')
