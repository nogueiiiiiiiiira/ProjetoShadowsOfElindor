import time

def escrever_lentamente(texto, atualizarGrafico):
    for i in range(0, len(texto) + 1, 2):  #
        atualizarGrafico(texto[:i])  
        time.sleep(0.0000005) 
    atualizarGrafico(texto)  

    pass
