import time
import sys

# Função para simular a escrita lenta na tela
def escrever_lentamente(texto, velocidade = 0.003):
    for char in texto:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(velocidade)
    print()
    
    pass
