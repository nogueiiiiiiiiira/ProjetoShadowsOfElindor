import time
import sys
import textwrap

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
