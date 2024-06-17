import pygame
import random

# Inicialização do Pygame
pygame.init()

# Cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Dimensões da tela
largura_tela = 640
altura_tela = 480

# Tamanho dos blocos da cobrinha
tamanho_bloco = 20

# Velocidade da cobrinha
velocidade = 10

# Inicialização da tela do jogo
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Jogo da Cobrinha")

# Relógio para controlar a atualização de tela
clock = pygame.time.Clock()

# Função para desenhar a cobrinha
def desenhar_cobrinha(cor, lista_cobra):
    for bloco in lista_cobra:
        pygame.draw.rect(tela, cor, [bloco[0], bloco[1], tamanho_bloco, tamanho_bloco])

# Função principal do jogo
def jogo():
    # Posição inicial da cobrinha
    x = largura_tela / 2
    y = altura_tela / 2

    # Velocidade inicial da cobrinha
    delta_x = 0
    delta_y = 0

    # Lista que guarda as partes da cobrinha
    lista_cobra = []
    comprimento_cobra = 1

    # Posição inicial da maçã
    maca_x = round(random.randrange(0, largura_tela - tamanho_bloco) / 20.0) * 20.0
    maca_y = round(random.randrange(0, altura_tela - tamanho_bloco) / 20.0) * 20.0

    # Flag para controle do jogo
    fim_jogo = False

    # Loop principal do jogo
    while not fim_jogo:
        # Verifica eventos do Pygame
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_jogo = True
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT and delta_x != velocidade:
                    delta_x = -velocidade
                    delta_y = 0
                elif evento.key == pygame.K_RIGHT and delta_x != -velocidade:
                    delta_x = velocidade
                    delta_y = 0
                elif evento.key == pygame.K_UP and delta_y != velocidade:
                    delta_x = 0
                    delta_y = -velocidade
                elif evento.key == pygame.K_DOWN and delta_y != -velocidade:
                    delta_x = 0
                    delta_y = velocidade

        # Atualiza posição da cobrinha
        x += delta_x
        y += delta_y

        # Verifica colisão com as bordas da tela
        if x >= largura_tela or x < 0 or y >= altura_tela or y < 0:
            fim_jogo = True

        # Preenche a tela com a cor preta
        tela.fill(BLACK)

        # Desenha a maçã
        pygame.draw.rect(tela, RED, [maca_x, maca_y, tamanho_bloco, tamanho_bloco])

        # Cria uma lista para guardar as posições da cobrinha
        cabeca_cobra = []
        cabeca_cobra.append(x)
        cabeca_cobra.append(y)
        lista_cobra.append(cabeca_cobra)
        if len(lista_cobra) > comprimento_cobra:
            del lista_cobra[0]

        # Verifica colisão com o próprio corpo
        for bloco in lista_cobra[:-1]:
            if bloco == cabeca_cobra:
                fim_jogo = True

        # Desenha a cobrinha
        desenhar_cobrinha(WHITE, lista_cobra)

        # Atualiza a tela
        pygame.display.update()

        # Verifica colisão com a maçã
        if x == maca_x and y == maca_y:
            maca_x = round(random.randrange(0, largura_tela - tamanho_bloco) / 20.0) * 20.0
            maca_y = round(random.randrange(0, altura_tela - tamanho_bloco) / 20.0) * 20.0
            comprimento_cobra += 1

        # Controla a velocidade do jogo
        clock.tick(15)

    # Encerra o Pygame
    pygame.quit()

# Inicializa o jogo
jogo()
