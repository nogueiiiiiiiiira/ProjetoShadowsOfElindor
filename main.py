import os
import time
import curses
from colorama import init, Fore
import pyfiglet
from game.fases import fase1, fase2, fase3, fase4, fase5

init(autoreset=True)

def center_text(text, width):
    return text.center(width)

def print_title(stdscr):
    title = "SHADOWS OF                            ELINDOR"  
    creators = [
        "ABILIO BATISTA",
        "FELIPE CESCA",
        "JOÃO PICOLI",
        "KAREN NOGUEIRA"
    ]

    centered_title = "\n".join(center_text("                            " + line, 80) for line in pyfiglet.figlet_format(title, width=80).splitlines())

    height, width = stdscr.getmaxyx()

    if height >= 15 and width >= 80:
        stdscr.clear()
        
        max_line_width = width - 2
        
        try:
            # Borda superior
            stdscr.addstr(center_text("=" * 70, max_line_width) + "\n", curses.color_pair(1))
            stdscr.addstr(center_text("||" + "=" * 66 + "||", max_line_width) + "\n", curses.color_pair(1))
            stdscr.addstr("\n")

            # Título centralizado
            stdscr.addstr(centered_title + "\n", curses.color_pair(1))
            stdscr.addstr(center_text("JOGO FEITO POR:", max_line_width) + "\n\n", curses.color_pair(1))

            # Nomes dos criadores
            for creator in creators:
                stdscr.addstr(center_text(creator, max_line_width) + "\n", curses.color_pair(1))

            # Borda inferior
            stdscr.addstr("\n" + center_text("||" + "=" * 66 + "||", max_line_width) + "\n", curses.color_pair(1))
            stdscr.addstr(center_text("=" * 70, max_line_width) + "\n\n", curses.color_pair(1))
            stdscr.refresh()
        except curses.error:
            pass  # Ignora erros caso o texto não caiba na tela
    else:
        stdscr.clear()
        stdscr.addstr(0, 0, "Por favor, aumente o tamanho da janela para pelo menos 80x15.")
        stdscr.refresh()
    time.sleep(2)

def countdown_timer(stdscr, seconds):
    height, width = stdscr.getmaxyx()
    timer_y = 26
    timer_x = (width // 2) - 15

    if height > timer_y and width >= 40:
        for remaining_time in range(seconds, 0, -1):
            try:
                stdscr.addstr(timer_y, timer_x, f"O jogo iniciará em {remaining_time} segundos", curses.color_pair(1))
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
    
    print_title(stdscr)  
    countdown_timer(stdscr, 9)
    
    stdscr.clear()

if __name__ == "__main__":
    curses.wrapper(main)  
    fase1()
    fase2()
    fase3()
    fase4()
    fase5()
