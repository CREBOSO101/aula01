# Programa de gerenciamento de pessoas do Luiz Fernando de Sousa Carvalho

print("Bem-vindo ao programa de gerenciamento de pessoas do Luiz Fernando de Sousa Carvalho!")

# Lista para armazenar os colaboradores
lista_colaboradores = []
# Variável global para armazenar o id do colaborador
id_global = 0

# Função para cadastrar um novo colaborador
def cadastrar_colaborador(id):
    # Solicita informações do colaborador
    nome = input("Digite o nome do colaborador: ")
    setor = input("Digite o setor do colaborador: ")
    salario = float(input("Digite o salário do colaborador: "))
    # Cria um dicionário com as informações do colaborador
    colaborador = {"id": id, "nome": nome, "setor": setor, "salario": salario}
    # Adiciona o colaborador à lista de colaboradores
    lista_colaboradores.append(colaborador)

# Função para imprimir uma tabela com as informações dos colaboradores
def imprimir_tabela(colaboradores):
    # Imprime o cabeçalho da tabela
    print("\n| ID | NOME | SETOR | SALÁRIO |")
    print("|----|------|-------|---------|")
    # Imprime as informações dos colaboradores
    for colaborador in colaboradores:
        print("| {} | {} | {} | R$ {:.2f} |".format(colaborador["id"], colaborador["nome"], colaborador["setor"], colaborador["salario"]))
    print()

# Função para consultar informações dos colaboradores
def consultar_colaborador():
    # Solicita a opção desejada pelo usuário
    opcao = int(input("Qual opção deseja? 1. Consultar Todos / 2. Consultar por Id / 3. Consultar por Setor / 4. Retornar ao menu: "))
    if opcao == 1:
        # Exibe todos os colaboradores cadastrados em uma tabela
        imprimir_tabela(lista_colaboradores)
    elif opcao == 2:
        # Solicita o id do colaborador a ser consultado
        id = int(input("Digite o id do colaborador: "))
        # Procura o colaborador com o id informado e exibe suas informações em uma tabela
        for colaborador in lista_colaboradores:
            if colaborador["id"] == id:
                imprimir_tabela([colaborador])
                break
    elif opcao == 3:
        # Solicita o setor a ser consultado
        setor = input("Digite o setor: ")
        # Procura os colaboradores do setor informado e exibe suas informações em uma tabela
        setor_colaboradores = []
        for colaborador in lista_colaboradores:
            if colaborador["setor"] == setor:
                setor_colaboradores.append(colaborador)
        imprimir_tabela(setor_colaboradores)
    elif opcao == 4:
        # Retorna ao menu principal
        return
    else:
        print("Opção inválida")

# Função para remover um colaborador da lista
def remover_colaborador():
    # Solicita o id do colaborador a ser removido
    id = int(input("Digite o id do colaborador a ser removido: "))
    # Procura o colaborador com o id informado e remove-o da lista
    for i, colaborador in enumerate(lista_colaboradores):
        if colaborador["id"] == id:
            del lista_colaboradores[i]
            break

# Loop principal do programa
while True:
    # Solicita a opção desejada pelo usuário
    opcao = int(input("Qual opção deseja? 1. Cadastrar Colaborador / 2. Consultar Colaborador / 3. Remover Colaborador / 4. Encerrar Programa: "))
    if opcao == 1:
        # Incrementa o id global e cadastra um novo colaborador
        id_global += 1
        cadastrar_colaborador(id_global)
    elif opcao == 2:
        # Consulta informações dos colaboradores
        consultar_colaborador()
    elif opcao == 3:
        # Remove colaborador
        remover_colaborador()
    elif opcao == 4:
        break
    else:
        print("Opção inválida")
