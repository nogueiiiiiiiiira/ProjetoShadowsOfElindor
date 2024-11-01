# main.py

import matplotlib.pyplot as plt
from game.fases import fase1, fase2, fase3, fase4, fase5
import textwrap

def atualizarGrafico(texto):
    plt.clf()  
    
    fig = plt.gcf()
    fig.patch.set_facecolor('black')
    
    ax = plt.gca()
    ax.set_facecolor('black')  
    ax.tick_params(colors='black') 
    
    # Quebra o texto em linhas e define o estilo da fonte Comic Sans
    linhas = textwrap.wrap(texto, width=60)
    texto_formatado = "\n".join(linhas)
    
    plt.text(
        0.5, 0.5, texto_formatado,
        fontsize=14, color='white', ha='center', va='center', 
        fontname='Comic Sans MS',  # Fonte Comic Sans MS
        fontweight='bold'
    )
    
    plt.axis('off')
    plt.pause(0.00001)  
    
def main():
    plt.ion()  
    plt.figure()

    fase1(atualizarGrafico)
    fase2(atualizarGrafico)
    fase3(atualizarGrafico)
    fase4(atualizarGrafico)
    fase5(atualizarGrafico)

    plt.ioff()  
    plt.show()  

if __name__ == "__main__":
    main()
