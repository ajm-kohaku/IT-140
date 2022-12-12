import curses
import json
import os
import sys
import textwrap
from curses import wrapper

MIN_CONSOLE_WIDTH = 150
MIN_CONSOLE_HEIGHT = 30


def load_game_data(filename):
    if not os.path.exists(filename):
        print('File {} does not exist.'.format(filename))
        sys.exit(1)
    with open(filename) as json_file:
        return json.load(json_file)


def intro_text():
    return ('Welcome to Onmyoji! '
            'You are a young Onmyoudou practitioner in the late Heian Period of Japan. Time is running out to stop the emergence of the Great Serpent.'
            'The city\'s magical array needs to be activated to prevent the Serpent from fully manifesting and destroying the city.'
            'You must activate the array by placing these four tokens at shrines positioned around the city and obtaining 3 items to complete the ritual to seal the beast.'
            'You must hurry, the Serpent is already manifesting and the city is in danger! '
            'Each shrine has a statue of the Guardian God that protects that cardinal direction. '
            'Give the turtle token to Genbu, the Dragon token to Seiyruu, the Bird token to Suzaku, and the Tiger token to Byakko.'
            'Good luck! And may the spirits protect you!')

# set type to get intellisense
# make sure terminal is big enough so that we don't have to deal with a whole bunch of complicated error handling


def check_terminal(screen: 'curses._CursesWindow'):
    # get screen size
    h, w = screen.getmaxyx()

    while True:
        # print current terminal size
        screen.addstr(0, 0, f'your screensize is: {w} by {h}')
        if h < MIN_CONSOLE_HEIGHT:
            screen.addstr(
                1, 0, f'game needs more height. please make terminal taller')
        if w < MIN_CONSOLE_WIDTH:
            screen.addstr(
                2, 0, f'game needs more width. please make terminal wider')
        else:
            screen.move(2, 0)
            screen.clrtoeol()

        # print screen requirements
        screen.addstr(
            3, 1, f'screen requirements: {MIN_CONSOLE_WIDTH} by {MIN_CONSOLE_HEIGHT}')

       # recheck screen
        h, w = screen.getmaxyx()

        # exit if we're copacetic
        if h >= MIN_CONSOLE_HEIGHT and w >= MIN_CONSOLE_WIDTH:
            break

        # don't crash while resizing the window
        try:
            char = screen.get_wch()
        except:
            pass
        if char == '\r' or char == '\n' or char == None:
            continue

        # finally redraw the screen before looping over again..
        screen.refresh()
    screen.addstr('Done!')

# set some colors and other defaults


def setup_terminal(screen):
    check_terminal(screen)
    # 99 => purple | 237 => dark grey
    curses.init_pair(1, 99, 237)
    # 99 => purple
    curses.init_pair(2, 97, curses.COLOR_BLACK)


def display_text_window(text):
    win_width = MIN_CONSOLE_WIDTH - 10

    # format text so that it fits nicely inside a box
    formatted_text = textwrap.fill(
        text, width=win_width - 3, initial_indent='  ', subsequent_indent='  ', fix_sentence_endings=True)

    # get number of lines in the text, last line won't have a new line so adding 1 to the result
    num_lines = formatted_text.count('\n') + 1

    text_window = curses.newwin(num_lines + 4, win_width, 1, 1)
    text_window.bkgd(curses.color_pair(2))
    text_window.box()
    text_window.refresh()
    text_box = text_window.derwin(num_lines + 2, win_width - 2, 1, 1)
    text_box.bkgd(curses.color_pair(2))
    text_box.addstr(1, 1, formatted_text)
    text_box.refresh()
    return text_box

def get_starting_room():
    game_data = load_game_data('game_data.json')
    for key, val in game_data.items():
        ...

# stdscr -> standard screen keeping default name here. but renaming it to screen for easier typing everywhere else
def main(stdscr):
    # if the terminal is too small. the app will stay open until you get the right size then close.
    setup_terminal(stdscr)
    stdscr.clear()

    # if the terminal meets the min requirements, continue with the game...
    text_window = display_text_window(intro_text())
    text_window.getch()
    game_data = load_game_data('game_data.json')
    current_room = {key: 'start' for (key, value) in game_data.items()}
    text_window = display_text_window(current_room.get('description'))
    text_window.getch()

wrapper(main)
