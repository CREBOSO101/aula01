A = int(input('Digite o primeiro lado do triangulo: '))
B = int(input('Digite o segundo lado do triangulo: '))
C = int(input('Digite o terceiro lado do triangulo: '))

if (A > 0) and (B > 0) and (C > 0):
    if (A + B > C) and (A + C > B) and (B + C > A):
    # Se você chegou até aqui é porque o triângulo é válido!
        if A != B and A != C and B != C:
            print('Triangulo escaleno!')
        else:
            if A == B and A == C and B == C:
                print('Triângulo equilatero!')
            else:
                print('Triângulo isóceles!')
    else:
        print('Ao menos um dos valores indicados não servem para formar um triângulo')
else:
    print('Ao menos um dos valores indicados não servem para formar um triângulo')