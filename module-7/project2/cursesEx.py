# import curses
# import textwrap

# screen = curses.initscr()
# screen.immedok(True)

# try:
#     screen.border(0)

#     box1 = curses.newwin(20, 40, 6, 50)
#     box2 = curses.newwin(18,38,7,51)
#     box1.immedok(True)
#     box2.immedok(True)
#     text = "I want all of this text to stay inside its box. Why does it keep going outside its borders?"
#     text = "The quick brown fox jumped over the lazy dog."
#     text = "A long time ago, in a galaxy far, far away, there lived a young man named Luke Skywalker."
#     box1.box()
#     box2.addstr(1, 0, textwrap.fill(text, 38))

#     #box1.addstr("Hello World of Curses!")

#     screen.getch()

# finally:
#     curses.endwin()

import curses

def c_main(stdscr: 'curses._CursesWindow') -> int:
    if curses.has_colors():
        curses.use_default_colors()
        curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_WHITE)
        curses.init_pair(2, 84,232)

    stdscr.insstr(5,0, f'COLORS: {curses.COLORS}')
    stdscr.insstr(6,0, f'COLOR_PAIRS: {curses.COLOR_PAIRS}')

    name = ''
    name_done = False
    while True:
        stdscr.addstr(0,0, 'What is your name?', curses.color_pair(1))
        stdscr.clrtoeol()
        stdscr.addstr(' ')
        stdscr.addstr(name)
        if name_done:
            stdscr.addstr(1,0, f'OHAI {name}!', curses.color_pair(2))
        
        char = stdscr.get_wch()
        if name_done:
            return 0
        elif isinstance(char, str) and char.isprintable():
            name += char
        elif char == curses.KEY_BACKSPACE or char == '\x7f':
            name = name[:-1]
        elif char == '\r' or char == '\n':
            name_done = True
        else:
            raise AssertionError(repr(char))

    

def main() -> int:
    return curses.wrapper(c_main)

if __name__ == "__main__":
    main()

'''
# gets the size of the window
h, w = stdscr.getmaxyx()

# create text in the middle of the screen
x = w//2 - len(text)//2
y = h//2
'''