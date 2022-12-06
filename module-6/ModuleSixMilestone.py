'''
Amber Murphy
IT-140: 22EW22
Module 6: Module Six Milestone - Move between rooms

requirements:
* ✅ prompt the player to enter commands to move between the rooms or exit
* gameplay loop includes:
    * ✅ output that displays the curent room
    * ✅ decision branching that tells the game how ot handle different commands.
    * ✅ if the player enters "exit" the game should set their room to a room called "exit"
    * ✅ if a player enters an invalid command, the game should output an error message
        -- sidestepped this a little. using pick to limit possible inputs
* ✅ a way to end the gameplay loop once the player is in the "exit" room
'''
# A dictionary for the simplified dragon text game
# The dictionary links a room to other rooms.
rooms = {
    'Great Hall': {'South': 'Bedroom'},
    'Bedroom': {'North': 'Great Hall', 'East': 'Cellar'},
    'Cellar': {'West': 'Bedroom'}
}

def menu_prompt(options):
    prompt = ''
    for option in options:
        prompt += f'{option}\n'
    prompt += 'Exit'
    return prompt

def move(room):
    options = []
    for direction in rooms.get(room).keys():
        options.append(direction)
    options.append('Exit')
    options.append('')
    print('Type the direction you want to go.\n')
    text_options = '\n'.join(options)
    option = str(input(text_options))
    if option.title() in options:
        return option
    else:
        print('Invalid option. Try again.\n')

def main():
    current_room = 'Great Hall'
    
    while True:
        print(f'You are currently in the {current_room}')
        option = move(current_room)
        if option != None and option.title() == 'Exit':
            print('Taking you to the exit. Goodbye!')
            break
        if option == None:
            option = move(current_room)
        else:
            current_room = rooms.get(current_room).get(option.title())

main()