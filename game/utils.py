import time

def escrever_lentamente(texto, atualizarGrafico):
    for i in range(0, len(texto) + 1, 2):  #
        atualizarGrafico(texto[:i])  
        time.sleep(0.0000005) 
    atualizarGrafico(texto)  
    
# Função para simular a escrita lenta na tela
def escrever_lentamente(texto, velocidade = 0.003):
    for char in texto:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(velocidade)
    print()
    
    pass
