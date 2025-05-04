import time # importa a biblioteca time para criar delays
import sys # importa a biblioteca sys para sair do programa
import textwrap # importa a biblioteca textwrap para formatar o texto
import matplotlib.pyplot as plt # importa a biblioteca matplotlib para exibir imagens
import matplotlib.image as mpimg # importa a biblioteca matplotlib para exibir imagens
import os # importa a biblioteca os para limpar o console

LARGURA_TERMINAL = 110 # largura do terminal para o texto

def escrever_lentamente(texto, delay=0.05, espacosEsquerda=4):
    linhas = texto.split('\n')
    primeira_linha = True  # controla se está na primeira linha do terminal

    for linha in linhas:
        partes = textwrap.wrap(linha, width = LARGURA_TERMINAL - espacosEsquerda) # divide a linha em partes para caber no terminal
        for parte in partes:
            if primeira_linha:
                
                # pula duas linhas se estiver na primeira linha, dando um ar mais organizado ao jogo
                sys.stdout.write('\n\n')
                primeira_linha = False 

            sys.stdout.write(' ' * espacosEsquerda)  
            sys.stdout.flush()

            for char in parte:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(delay)
            sys.stdout.write('\n') 
            sys.stdout.flush()  # atualiza a tela

# mostra a imagem do personagem
def mostrar_imagem(nome_imagem):
    
    # carrega a imagem 
    img = mpimg.imread(f'imagens/{nome_imagem}')  
    
    # cria uma nova figura com fundo preto
    fig, ax = plt.subplots() # figura e eixo
    fig.patch.set_facecolor('black') # define o fundo da figura como preto
    ax.imshow(img) # exibe a imagem
    ax.axis('off') # desativa os eixos
    
    # define o fundo do eixo como preto
    ax.set_facecolor('black') # define o fundo do eixo como preto
    plt.show() # exibe a imagem na tela
    
def limpar_console():
    
    # verifica o sistema operacional
    if os.name == 'nt':  # Windows
        os.system('cls')
        
    else:  # macOS e Linux
        os.system('clear')
