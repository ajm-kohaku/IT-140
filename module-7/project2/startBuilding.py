import curses, textwrap
from curses.panel import new_panel, top_panel, update_panels
from curses.textpad import Textbox, rectangle

MIN_CONSOLE_WIDTH = 150
MIN_CONSOLE_HEIGHT = 30

def wait_to_quit(screen) -> int:
    while True:
        char = ''
        try:
            char = screen.get_wch()
        except:
            pass
        if  char == '\r' or char == '\n':
            return 0
        if char == None:
            continue

def check_terminal(stdscr: 'curses._CursesWindow') -> int:
    stdscr.addstr(0,0,'checking screen requirements...')
    set_terminal_requirements(stdscr)
    stdscr.clear()
    # stdscr.addstr(0,0,'terminal size looks good...')
    # wait_to_quit(stdscr)
    

def set_terminal_requirements(stdscr: 'curses._CursesWindow') -> int:
    # renaming system variable for readability
    screen = stdscr

    # get terminal max height & width
    h, w = screen.getmaxyx()

    screen.clear()
    while True:
        screen.addstr(0,0, f'your screensize is: {w} by {h}')
        # check width and height
        if h < MIN_CONSOLE_HEIGHT:
            screen.addstr(1,0, f'game needs more height. please make terminal taller')
        else:
            screen.move(1,0)
            screen.clrtoeol()
        if w < MIN_CONSOLE_WIDTH:
            screen.addstr(2, 0, f'game needs more width. please make terminal wider')
        else:
            screen.move(2,0)
            screen.clrtoeol()

        # print requirements
        screen.addstr(3,1, f'screen requirements: {MIN_CONSOLE_WIDTH} by {MIN_CONSOLE_HEIGHT}')
        
        # recheck screen
        h, w = screen.getmaxyx()

        # breakout if we're copacetic 
        if h >= MIN_CONSOLE_HEIGHT and w >= MIN_CONSOLE_WIDTH:
            screen.addstr(3,1, f'you meet the minimum screen requirements of {MIN_CONSOLE_WIDTH} by {MIN_CONSOLE_HEIGHT}')
            return 0
        
        # don't crash while resizing the window
        char = ''
        try:
            char = stdscr.get_wch()
        except:
            pass
        if  char == '\r' or char == '\n':
            return 0
        if char == None:
            continue
        screen.refresh()

def do_it(win):  # Shia LeBeouf!
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)
    win.bkgd(' ', curses.color_pair(1) | curses.A_BOLD)
    win.addstr(1,1, "This is not blue")
    win.getch()
    win.bkgd(' ', curses.color_pair(1) | curses.A_BOLD | curses.A_REVERSE)
    win.addstr(1,1, "This is now blue")
    win.getch()

def setup_terminal(screen, text) -> dict:
    if curses.has_colors:
        curses.use_default_colors()
        # purple foreground on grey background
    curses.init_pair(1, 99, 237)
    
    win = text_window(screen, text)
    win.getch()

def text_window(screen: 'curses._CursesWindow', text):
    WIN_HEIGHT = MIN_CONSOLE_HEIGHT - 15
    WIN_WIDTH = MIN_CONSOLE_WIDTH - 10
    formatted_text = textwrap.fill(text, width=WIN_WIDTH - 2, initial_indent='  ', subsequent_indent='  ')
    num_lines = 0
    for char in formatted_text:
        if char == '\n':
            num_lines+=1
    print(num_lines)
    box1 = curses.newwin(num_lines + 5, WIN_WIDTH, 1, 1)
    box1.box()
    box1.refresh()
    # derwin is relative to the parent window:
    box2 = box1.derwin(num_lines + 3, WIN_WIDTH -2, 1,1)
    box2.addstr(1, 1, f'{formatted_text}')
    box2.refresh()
    return box2
         

def tossed_terminal(screen, text):
    if curses.has_colors():
        curses.use_default_colors()
        # purple foreground on grey background
        curses.init_pair(1, 99, 237)
    screen.bkgd(' ', curses.color_pair(1))
    screen.refresh()
    check_terminal(screen)
    #   min_height = 20
    #   min_width = 100
    main_window = curses.newwin(18, 98, 0, 0)
    main_window.bkgd(' ', curses.color_pair(1))
    # main_window.addstr(1, 1, text)

    text_window = curses.newpad(15,98)
    text_window.bkgd(' ', curses.color_pair(1))
    text_window.addstr(1,0, text)
    text_window.refresh(0,0, 1,0, 15,98)
    # main_window.refresh()
    text_window.getch()



def get_colors(stdscr):
    curses.start_color()
    curses.use_default_colors()  
    for i in range(0, curses.COLORS):
        curses.init_pair(i + 1, i, 237)
    stdscr.addstr(0, 0, '{0} colors available'.format(curses.COLORS))
    maxy, maxx = stdscr.getmaxyx()
    maxx = maxx - maxx % 5
    x = 0
    y = 1
    try:
        for i in range(0, curses.COLORS):
            stdscr.addstr(y, x, '{0:5}'.format(i), curses.color_pair(i))
            x = (x + 5) % maxx
            if x == 0:
                y += 1
    except curses.ERR:
        pass
    stdscr.getch()

def intro_text():
    return ('Welcome to the Text Based Game!'
            'You are a young Onmyoudou practitioner in the late Heian Period and time is running out to stop the emergence of the Great Serpent.'
            'The city\'s great magical array needs to be activated to prevent the serpent from fully manifesting and destroying the city.'
            'You have been given four tokens '
            'You must hurry, the serpent is already manifesting and the city is in danger!'
            'Each shrine has a statue of the guardian god that protections that cardinal direction.'
            'In order from North moving clockwise there\'s; Genbu, Seiyruu, Suzaku, and Byakko.')

def main(stdscr):
    setup_terminal(stdscr, intro_text())




curses.wrapper(main)