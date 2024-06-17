def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while ((x < min) or (x > max)):
        x = int(input(pergunta))
    return x

def criaarquivo(nomearquivo):
    try:
        a = open(nomearquivo, 'wt+')
        a.close()
    except:
        print('Erro na criação do arquivo')
    else:
        print('Arquivo {} foi criado com sucesso!\n'.format(nomearquivo))

def existearquivo(nomearquivo):
    try:
        a = open(nomearquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def listararquivo(nomearquivo):
    try:
        a = open(nomearquivo, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        print(a.read())
    finally:
        a.close()

def cadastrarjogo(nomearquivo, nomejogo, nomevideogame):
    try:
        a = open(nomearquivo, 'at')
    except:
        print('Erro ao abrir o arquivo')
    else:
        a.write('{};{}\n'.format(nomejogo,nomevideogame))
    finally:
        a.close()

#Programa principal
arquivo = 'games.txt'
if existearquivo(arquivo):
    print('Arquivo localizado no computador')
else:
    print('Arquivo inexistente')
    criaarquivo(arquivo)

while True:
    print('MENU')
    print('1 - Cadastrar novo item')
    print('2 - Listar cadastros')
    print('3 - Sair')

    op = valida_int('Escolha a opção desejada: ', 1, 3)
    if op == 1:
        print('Opção de cadastrar novo item selecionado...\n')
        nomejogo = input('Nome do jogo: ')
        nomevideogame = input('Nome do videogame: ')
        cadastrarjogo(arquivo, nomejogo, nomevideogame)
    elif op == 2:
        print('Opção de listar selecionado...\n')
        listararquivo(arquivo)
    elif op == 3:
        print('Encerrando o programa...')
        break