import time # importa a biblioteca time para usar o sleep
import curses # importa a biblioteca curses para manipulação de terminal
from colorama import init # importa a biblioteca colorama para manipulação de cores no terminal
import pyfiglet # importa a biblioteca pyfiglet para gerar texto em arte ASCII
from game.fases import instrucoes, fase1, fase2, fase3, fase4, fase5 # importa as fases do jogo

init(autoreset=True) # inicia a biblioteca colorama

def texto_centralizado(text, largura): # função para centralizar o texto no terminal
    return text.center(largura) # centraliza o texto em uma largura específica

def print_titulo(tela): # função para imprimir o título e os criadores do jogo.
    titulo = "                   SHADOWS                                                OF                                                     ELINDOR"  
    criadores = [
        "ABILIO BATISTA",
        "FELIPE CESCA",
        "JOÃO PICOLI",
        "KAREN NOGUEIRA"
    ]

    # converte o título para arte ASCII
    titulo_centralizado = "\n".join(texto_centralizado("                            " + line, 80) for line in pyfiglet.figlet_format(titulo, largura=80).splitlines())

    # inicializa a tela
    altura, largura = tela.getmaxyx()

    if altura >= 15 and largura >= 80:
        tela.clear()
        
        maximo_linha_largura = largura - 2
        
        try:
            # borda superior com os ===================
            tela.addstr(texto_centralizado("=" * 70, maximo_linha_largura) + "\n", curses.color_pair(1))
            tela.addstr(texto_centralizado("||" + "=" * 66 + "||", maximo_linha_largura) + "\n", curses.color_pair(1))
            tela.addstr("\n")

            # titulo centralizado com cor verde
            tela.addstr(titulo_centralizado + "\n", curses.color_pair(2)) # verde
            tela.addstr(texto_centralizado("\n                                                              JOGO FEITO POR:", maximo_linha_largura) + "\n\n", curses.color_pair(1))

            # nomes dos criadores
            for criador in criadores:
                tela.addstr(texto_centralizado(criador, maximo_linha_largura) + "\n", curses.color_pair(1))

            # borda inferior com os ========================
            tela.addstr("\n" + texto_centralizado("||" + "=" * 66 + "||", maximo_linha_largura) + "\n", curses.color_pair(1))
            tela.addstr(texto_centralizado("=" * 70, maximo_linha_largura) + "\n\n", curses.color_pair(1))
            tela.refresh()
        except curses.error:
            pass  # ignora erros caso o texto não caiba na tela
    else:
        tela.clear() 
        tela.addstr(0, 0, "Por favor, aumente o tamanho da janela para pelo menos 80x15.") # tamanho mínimo para o jogo funcionar corretamente
        tela.refresh() # atualiza a tela
    time.sleep(2)

def mensagem_final(tela):
    tela.clear()
    mensagem_final = "                              OBRIGADO                                                 POR                                                  JOGAR !"
    mensagem_ascii = pyfiglet.figlet_format(mensagem_final, largura=80) # converte a mensagem para arte ASCII
    tela.addstr(mensagem_ascii, curses.color_pair(2)) # verde
    tela.refresh()
    time.sleep(10)  
    
def contador(tela, segundos): # função para criar um contador regressivo
    altura, largura = tela.getmaxyx() # obtém a altura e largura da tela
    timer_y = 32 # posição y do timer
    timer_x = (largura // 2) - 15 # posição x do timer (centralizado na tela)

    if altura > timer_y and largura >= 40: # verifica se a tela é grande o suficiente
        for tempo_restante in range(segundos, 0, -1): # inicia o contador regressivo
            try:
                tela.addstr(timer_y, timer_x, f"O jogo iniciará em {tempo_restante} segundos", curses.color_pair(1)) # exibe o tempo restante
                tela.refresh() 
                time.sleep(1)
            except curses.error: # ignora erros caso o texto não caiba na tela
                pass
    else:
        tela.clear()
        tela.addstr(0, 0, "Aumente a janela para exibir o contador.")
        tela.refresh()
        time.sleep(2)

def main(tela): # função principal que inicializa o jogo
    curses.start_color() # inicializa as cores
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)  # define a cor branca
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)  # define a cor verde
    
    print_titulo(tela) # exibe o título do jogo
    
    contador(tela, 9) # inicia o contador regressivo

    
    tela.clear()

if __name__ == "__main__": # verifica se o script está sendo executado diretamente
    
    curses.wrapper(main)  # chama a função principal do jogo
    
    instrucoes() # exibe as instruções do jogo
    fase1() # inicia a primeira fase do jogo
    fase2() # inicia a segunda fase do jogo
    fase3() # inicia a terceira fase do jogo
    fase4() # inicia a quarta fase do jogo
    fase5() # inicia a quinta fase do jogo
    
    curses.wrapper(mensagem_final) # exibe a mensagem final do jogo
