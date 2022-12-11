import curses, json,os,sys, textwrap
from curses.textpad import Textbox, rectangle
from curses import wrapper

def load_game_data(filename):
    if not os.path.exists(filename):
        print('File {} does not exist.'.format(filename))
        sys.exit(1)

    with open(filename) as json_file:
        return json.load(json_file)

def intro_text():
    return ('Welcome to the Text Based Game!\n'
            'You are a young Onmyoudou practitioner in the late Heian Period and time is running out to stop the emergence of the Great Serpent.'
            'The city\'s great magical array needs to be activated to prevent the serpent from fully manifesting and destroying the city.'
            'You have been given four tokens \n'
            'You must hurry, the serpent is already manifesting and the city is in danger!\n'
            'Each shrine has a statue of the guardian god that protections that cardinal direction.'
            'In order from North moving clockwise there\'s; Genbu, Seiyruu, Suzaku, and Byakko.')



def main(screen):
    win = curses.newwin(15, 75, 2, 2)
    box = Textbox(win)

    rectangle(screen, 1, 1, 18, 78)
    screen.refresh()

    box.edit()
    text = intro_text()

    screen.addstr(7, 2, text)
    screen.getch()

wrapper(main)