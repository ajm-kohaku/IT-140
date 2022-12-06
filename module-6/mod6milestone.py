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