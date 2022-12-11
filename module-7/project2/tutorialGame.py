import cmd, textwrap, sys, os, time, random

screen_width = 100

#### Player Setup ####
class player:
    def __init__(self):
        self.name = ''
        self.hp = 0
        self.mp = 0
        self.status_effects = []

myPlayer = player()

#### Title Screen ####
def title_screen_selections():
    option = ('> ')
    option_stuff(option)
    while option not in ['play', 'help', 'quit']:
        print('please enter a valid command')
        option = input('> ')
        option_stuff(option)

def title_screen():
    os.system('clear')
    print('###########################')
    print('# Welcome to the Text RPG!#')
    print('###########################')
    print('            - Play        ')
    print('            - Help        ')
    print('            - Quit        ')
    print(' Copywright 2022 kohaku.me')
    title_screen_selections()

def help_menu():
    print('###########################')
    print('# Welcome to the Text RPG!#')
    print('###########################')
    print(' - Use up, down, left, right to move')
    print(' - Type your commands to do them')
    print(' - Use "look" to inspect something')
    print(' - Good luck and have fun!')
    title_screen_selections()

def option_stuff(option):
    option = option.lower()
    if option == 'play':
        start_game() # placeholder until written
    elif option == 'help':
        help_menu()
    elif option == 'quit':
        sys.exit()