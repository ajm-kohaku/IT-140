command = input("What are you doing next? ")
# analyze the result of command.split()

[action, obj] = command.split()
... # interpret action, obj

match command.split():
    case ["quit"]:
        print("Goodbye!")
        # quit_game()
    case ["look"]:
        print('room description')
    case ["get", obj]:
        #character.get(obj, current_room)
        print('get obj')
    case ["go", direction]:
        print('go direction')
        #current_room = current_room.neighbor(direction)
    # The rest of your commands go here