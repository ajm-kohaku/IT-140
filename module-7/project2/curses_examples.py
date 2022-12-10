import curses
import time
from curses import wrapper
from curses.textpad import Textbox, rectangle


def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_YELLOW)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_WHITE)
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)

    BLUE_AND_YELLOW = curses.color_pair(1)
    RED_AND_WHITE = curses.color_pair(2)
    GREEN = curses.color_pair(3)


wrapper(main)

def window(stdscr, color1, color2):
    stdscr.addstr('Hello World')
    stdscr.refresh()

    # coordinates are (y, x)
    counter_window = curses.newwin(1, 20, 10, 10)

    for i in range(75):
        counter_window.clear()
        color = color1 if i % 2 == 0 else color2
        counter_window.addstr(f'Count: {i}', color)
        counter_window.refresh()
        time.sleep(0.1)


def pad(stdscr, color):
    pad = curses.newpad(100, 100)
    stdscr.refresh()

    for i in range(100):
        for j in range(26):
            char = chr(67+j)
            pad.addstr(char, color)

    pad.refresh(0, 0, 5, 5, 20, 25)

def create_rectangle_with_text(stdscr, color):
    win = curses.newwin(3, 18, 2, 2)
    box = Textbox(win)

    rectangle(stdscr, 1, 1, 5, 20)
    stdscr.refresh()

    box.edit()
    text = box.gather().replace('\n', '').strip()

    stdscr.addstr(7, 2, text, color)
    stdscr.getch()


def move_cursor(stdscr, color):
    stdscr.nodelay(True)
    x, y = 0, 0
    while True:

        try:
            key = stdscr.getkey()
        except:
            key = None

        if key == 'KEY_UP':
            y -= 1
        elif key == 'KEY_DOWN':
            y += 1
        elif key == 'KEY_LEFT':
            x -= 1
        elif key == 'KEY_RIGHT':
            x += 1
        elif key == 'q':
            break

        stdscr.clear()
        stdscr.addstr(y, x, 'X', color)
        stdscr.refresh()
