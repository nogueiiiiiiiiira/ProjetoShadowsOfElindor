import time
import curses
from colorama import init
import pyfiglet
from game.fases import instrucoes, fase1, fase2, fase3, fase4, fase5

init(autoreset=True)

def textoCentralizado(text, width):
    return text.center(width)

def print_title(stdscr):
    title = "                   SHADOWS                                                OF                                                     ELINDOR"  
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
            # borda superior com os ===================
            stdscr.addstr(textoCentralizado("=" * 70, max_line_width) + "\n", curses.color_pair(1))
            stdscr.addstr(textoCentralizado("||" + "=" * 66 + "||", max_line_width) + "\n", curses.color_pair(1))
            stdscr.addstr("\n")

            # titulo centralizado com cor verde
            stdscr.addstr(tituloCentralizado + "\n", curses.color_pair(2)) # verde
            stdscr.addstr(textoCentralizado("\n                                                              JOGO FEITO POR:", max_line_width) + "\n\n", curses.color_pair(1))

            # nomes dos criadores
            for creator in creators:
                stdscr.addstr(textoCentralizado(creator, max_line_width) + "\n", curses.color_pair(1))

            # borda inferior com os ========================
            stdscr.addstr("\n" + textoCentralizado("||" + "=" * 66 + "||", max_line_width) + "\n", curses.color_pair(1))
            stdscr.addstr(textoCentralizado("=" * 70, max_line_width) + "\n\n", curses.color_pair(1))
            stdscr.refresh()
        except curses.error:
            pass  # ignora erros caso o texto não caiba na tela
    else:
        stdscr.clear()
        stdscr.addstr(0, 0, "Por favor, aumente o tamanho da janela para pelo menos 80x15.")
        stdscr.refresh()
    time.sleep(2)

def mensagemFinal(stdscr):
    stdscr.clear()
    mensagem_final = "                              OBRIGADO                                                 POR                                                  JOGAR !"
    mensagem_ascii = pyfiglet.figlet_format(mensagem_final, width=80)
    stdscr.addstr(mensagem_ascii, curses.color_pair(2)) 
    stdscr.refresh()
    time.sleep(10)  
    
def contador(stdscr, segundos):
    height, width = stdscr.getmaxyx()
    timer_y = 32
    timer_x = (width // 2) - 15

    if height > timer_y and width >= 40:
        for tempoRestante in range(segundos, 0, -1):
            try:
                stdscr.addstr(timer_y, timer_x, f"O jogo iniciará em {tempoRestante} segundos", curses.color_pair(1))
                stdscr.refresh()
                time.sleep(1)
            except curses.error:
                pass
    else:
        stdscr.clear()
        stdscr.addstr(0, 0, "Aumente a janela para exibir o contador.")
        stdscr.refresh()
        time.sleep(2)

def main(stdscr):
    curses.start_color()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK) 
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK) 
    
    print_title(stdscr)  
    
    contador(stdscr, 9)

    
    stdscr.clear()

if __name__ == "__main__":
    
    curses.wrapper(main) 
    
    instrucoes()
    fase1()
    fase2()
    fase3()
    fase4()
    fase5()
    
    curses.wrapper(mensagemFinal)
