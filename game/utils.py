import time
import sys
import textwrap
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os

LARGURA_TERMINAL = 110

def escreverLentamente(texto, delay=0.05, espacosEsquerda=4):
    linhas = texto.split('\n')
    primeiraLinha = True  # controla se está na primeira linha do terminal

    for linha in linhas:
        partes = textwrap.wrap(linha, width = LARGURA_TERMINAL - espacosEsquerda)
        for parte in partes:
            if primeiraLinha:
                
                # pula duas linhas se estiver na primeira linha, dando um ar mais organizado ao jogo
                sys.stdout.write('\n\n')
                primeiraLinha = False 

            sys.stdout.write(' ' * espacosEsquerda)  
            sys.stdout.flush()

            for char in parte:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(delay)
            sys.stdout.write('\n') 
            sys.stdout.flush()  # atualiza a tela

# mostra a imagem do personagem
def mostrarImagem(nomeImagem):
    
    # carrega a imagem 
    img = mpimg.imread(f'imagens/{nomeImagem}')  
    
    # cria uma nova figura com fundo preto
    fig, ax = plt.subplots()
    fig.patch.set_facecolor('black') 
    ax.imshow(img)
    ax.axis('off') 
    
    # define o fundo do eixo como preto
    ax.set_facecolor('black')
    plt.show()
    
def limparConsole():
    
    # verifica o sistema operacional
    if os.name == 'nt':  # Windows
        os.system('cls')
        
    else:  # macOS e Linux
        os.system('clear')
