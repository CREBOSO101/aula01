# Inicio das variaveis globais
lista_produtos = []
codigo_produto = 0

# Inicio de cadastrar_produto()
def cadastrar_produto(codigo):
  print('Bem vindo ao menu de Cadastrar Produtos')
  print('Código do Produto: {}'.format(codigo))
  nome = input('Entre com o NOME do produto: ')
  fabricante = input('Entre com o FABRICANTE do produto: ')
  preco = int(input('Entre com o PREÇO(R$) do produto: '))
  dicionario_produto= {'codigo'      : codigo,
                        'nome'        : nome,
                        'fabricante'  : fabricante,
                        'preco'       : preco}
  lista_produtos.append(dicionario_produto.copy())

# Inicio de consultar_produto()
def consultar_produto():
  print('Bem vindo ao menu de Consultar Produtos')
  while True:
    opcao_consultar = input('\nEscolha a opção desejada:\n'+
                            '1- Consultar TODOS os produtos\n'+
                            '2- Consultar produto por CÓDIGO\n'+
                            '3- Consultar produto(s) por FABRICANTE\n'+
                            '4- Retornar\n'+
                            '>>')
    if opcao_consultar == '1':
      print('Você escolheu a opção Consultar TODOS os produtos')
      for produto in lista_produtos:
          print('--------------------')
          for key, value in produto.items():
              print('{}: {}'.format(key,value))
          print('--------------------')
    elif opcao_consultar == '2':
      print('Você escolheu a opção Consultar produto por código ')
      valor_desejado = int(input('Entre com o Código desejado: '))
      for produto in lista_produtos:
          if produto['codigo'] == valor_desejado:
              print('--------------------')
              for key, value in produto.items():
                  print('{}: {}'.format(key, value))
              print('--------------------')
    elif opcao_consultar == '3':
      print('Você escolheu a opção Consultar produto(s) por fabricante')
      valor_desejado = input('Entre com o fabricante desejado: ')
      for produto in lista_produtos:
          if produto['fabricante'] == valor_desejado:
              print('--------------------')
              for key, value in produto.items():
                  print('{}: {}'.format(key, value))
              print('--------------------')
    elif opcao_consultar == '4':
      return
    else:
      print('Opção Inválida. Tente novamente')
      continue
# Inicio de remover_produto()
def remover_produto():
  print('Bem vindo ao menu de Remover Produtos')
  valor_desejado = int(input('Entre com o código do produto que deseja remover: '))
  for produto in lista_produtos:
      if produto['codigo'] == valor_desejado:
          lista_produtos.remove(produto)
          print('Produto removido')
# Inicio de Main
print('Bem vindo a Mercearia do Luiz Fernando')
while True:
  opcao_principal = input('\nEscolha a opção desejada:\n'+
                          '1- Cadastrar produto\n'+
                          '2- Consultar produto(s)\n'+
                          '3- Remover produto\n'+
                          '4- Sair\n'+
                          '>>')
  if opcao_principal == '1':
    codigo_produto = codigo_produto + 1
    cadastrar_produto(codigo_produto)
  elif opcao_principal == '2':
    consultar_produto()
  elif opcao_principal == '3':
    remover_produto()
  elif opcao_principal == '4':
    break
  else:
    print('Opção Inválida. Tente novamente')
    continue
