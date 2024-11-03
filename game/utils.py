import time
import sys
import textwrap
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

LARGURA_TERMINAL = 110

def escrever_lentamente(texto, delay=0.000000000000000000005, espacos_esquerda=4):
    linhas = texto.split('\n')
    primeira_linha = True  # Controla se está na primeira linha do terminal

    for linha in linhas:
        partes = textwrap.wrap(linha, width=LARGURA_TERMINAL - espacos_esquerda)
        for parte in partes:
            if primeira_linha:
                # Pula duas linhas se estiver na primeira linha
                sys.stdout.write('\n\n')
                primeira_linha = False  # Após a primeira linha, não precisa mais pular

            sys.stdout.write(' ' * espacos_esquerda)  # Indentação à esquerda
            sys.stdout.flush()

            for char in parte:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(delay)
            sys.stdout.write('\n')  # Nova linha após a parte completa
            sys.stdout.flush()  # Atualiza a tela

# Função para mostrar a imagem do personagem
def mostrar_imagem_personagem(nome_imagem):
    img = mpimg.imread(f'imagens/{nome_imagem}')  # Certifique-se de ajustar o caminho da imagem
    plt.imshow(img)
    plt.axis('off')  # Remove os eixos para melhor visualização
    plt.show()
    
