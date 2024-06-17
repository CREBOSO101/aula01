import random

def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while ((x < min) or (x > max)):
        x = int(input(pergunta))
    return x

def vencedor(jogador1, jogador2):
    global empate, v1, v2
    if jogador1 == 1:
        if jogador2 == 1:
            empate += 1
        elif jogador2 == 2:
            v2 += 1
        elif jogador2 == 3:
            v1 += 1
    elif jogador1 == 2:
        if jogador2 == 1:
            v1 += 1
        elif jogador2 == 2:
            empate += 1
        elif jogador2 == 3:
            v2 += 1
    elif jogador1 == 3:
        if jogador2 == 1:
            v2 +=1
        elif jogador2 == 2:
            v1 += 1
        elif jogador2 == 3:
            empate += 1
    resultados = [v1, v2, empate]
    return resultados

#Programa principal
print('JOKENPÔ')
print('1 - Pedra')
print('2 - Papel')
print('3 - Tesoura')

resultados = []
jogadas = []
v1 = 0
v2 = 0
empate= 0

while True:
    j1 = valida_int('Escolha sua jogada: ', 0, 3)
    if not j1:
        break
    j2 = random.randint(1,3)
    jogadas.append([j1, j2])
    resultados = vencedor(j1, j2)
    #print(vencedor(j1, j2))

    for jogada in jogadas:
        for dado in jogada:
            print(dado, end=' ')
        print()

print('Numero de vitórias do jogador 1: {}'.format(resultados[0]))
print('Numero de vitórias do jogador 2: {}'.format(resultados[1]))
print('Numero de empates: {}'.format(resultados[2]))