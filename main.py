import os
import time
import curses
from colorama import init
import pyfiglet
from game.fases import instrucoes, fase1, fase2, fase3, fase4, fase5

init(autoreset=True)

def textoCentralizado(text, width):
    return text.center(width)

def print_title(stdscr):
    title = "SHADOWS OF                            ELINDOR"  
    creators = [
        "ABILIO BATISTA",
        "FELIPE CESCA",
        "JOÃO PICOLI",
        "KAREN NOGUEIRA"
    ]

    tituloCentralizado = "\n".join(textoCentralizado("                            " + line, 80) for line in pyfiglet.figlet_format(title, width=80).splitlines())

    height, width = stdscr.getmaxyx()

    if height >= 15 and width >= 80:
        stdscr.clear()
        
        max_line_width = width - 2
        
        try:
            # Borda superior
            stdscr.addstr(textoCentralizado("=" * 70, max_line_width) + "\n", curses.color_pair(1))
            stdscr.addstr(textoCentralizado("||" + "=" * 66 + "||", max_line_width) + "\n", curses.color_pair(1))
            stdscr.addstr("\n")

            # Título centralizado com cor verde
            stdscr.addstr(tituloCentralizado + "\n", curses.color_pair(2))  # Usando o par de cores 2 (verde)
            stdscr.addstr(textoCentralizado("\n                                                    JOGO FEITO POR:", max_line_width) + "\n\n", curses.color_pair(1))

            # Nomes dos criadores
            for creator in creators:
                stdscr.addstr(textoCentralizado(creator, max_line_width) + "\n", curses.color_pair(1))

            # Borda inferior
            stdscr.addstr("\n" + textoCentralizado("||" + "=" * 66 + "||", max_line_width) + "\n", curses.color_pair(1))
            stdscr.addstr(textoCentralizado("=" * 70, max_line_width) + "\n\n", curses.color_pair(1))
            stdscr.refresh()
        except curses.error:
            pass  # Ignora erros caso o texto não caiba na tela
    else:
        stdscr.clear()
        stdscr.addstr(0, 0, "Por favor, aumente o tamanho da janela para pelo menos 80x15.")
        stdscr.refresh()
    time.sleep(2)

def mostrar_mensagem_final(stdscr):
    stdscr.clear()
    mensagem_final = "                              OBRIGADO                                                 POR                                                  JOGAR !"
    mensagem_ascii = pyfiglet.figlet_format(mensagem_final, width=80)
    stdscr.addstr(mensagem_ascii, curses.color_pair(2))  # Mensagem em verde
    stdscr.refresh()
    time.sleep(10)  # Espera 5 segundos para o jogador ver a mensagem

def main(stdscr):
    curses.start_color()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)  # Branco no fundo preto
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)  # Verde no fundo preto
    
    print_title(stdscr)  
    
    stdscr.clear()

if __name__ == "__main__":
    curses.wrapper(main)  # Inicializa a interface curses
    
    # Executa as fases do jogo
    
    instrucoes()
    fase1()
    fase2()
    fase3()
    fase4()
    fase5()
    
    # Mostra a mensagem de agradecimento ao final do jogo
    curses.wrapper(mostrar_mensagem_final)