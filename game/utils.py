import time
import sys
import textwrap
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os

LARGURA_TERMINAL = 110

def escreverLentamente(texto, delay=0.000000000000000000005, espacosEsquerda=4):
    linhas = texto.split('\n')
    primeiraLinha = True  # Controla se está na primeira linha do terminal

    for linha in linhas:
        partes = textwrap.wrap(linha, width = LARGURA_TERMINAL - espacosEsquerda)
        for parte in partes:
            if primeiraLinha:
                
                # Pula duas linhas se estiver na primeira linha
                sys.stdout.write('\n\n')
                primeiraLinha = False 

            sys.stdout.write(' ' * espacosEsquerda)  
            sys.stdout.flush()

            for char in parte:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(delay)
            sys.stdout.write('\n') 
            sys.stdout.flush()  # Atualiza a tela

# Função para mostrar a imagem do personagem
def mostrarImagem(nomeImagem):
    # Carrega a imagem da pasta 'imagens'
    img = mpimg.imread(f'imagens/{nomeImagem}')  
    
    # Cria uma nova figura com fundo preto
    fig, ax = plt.subplots()
    fig.patch.set_facecolor('black')  # Define o fundo da figura como preto
    ax.imshow(img)
    ax.axis('off')  # Remove os eixos
    
    # Define o fundo do eixo como preto
    ax.set_facecolor('black')
    plt.show()
    
def limparConsole():
    # Verifica o sistema operacional
    if os.name == 'nt':  # Windows
        os.system('cls')
        
    else:  # macOS e Linux
        os.system('clear')

# Exemplo de uso
limparConsole()
