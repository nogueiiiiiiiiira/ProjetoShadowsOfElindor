import time
import sys

# Função para simular a escrita lenta na tela
def escrever_lentamente(texto, velocidade = 0.05):
    for char in texto:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(velocidade)
    print()
    
    pass
