world_map = {
    'R19A': {
        'NAME': "Mr. Wade's Room",
        'DESCRIPTION': "THis is the room you are in",
        'PATHS': {
            'NORTH': "PARKING_LOT"

        }

    },
    'PARKING_LOT': {
        'NAME': "A Parking Lot",
        'DESCRIPTION': "THere are a few cars parked here",
        'PATHS': {
            'SOUTH': 'R19A'
        }
    },
    'AMPHITHEATER': {
        'NAME': "The Stage outside",
        'DESCRIPTION': "There might be some items here",
        'PATHS': {
            'SOUTH': 'R19A'
        }
    },
    'CAFETERIA': {
        'NAME': "The place to get food and chill",
        'DESCRIPTION': "There is some leftover non eaten ham and cheese bars and there might"
                       "be some items here",
        'PATHS': {
            'SOUTH': 'AMPHITHEATER'
        }
    }





}

# Other Variables
directions = ["NORTH", "SOUTH", "EAST", "WEST", "UP"]
current_node = world_map["R19A"]  # THis is your current location
playing = True

# Controller
while playing:
    print(current_node['NAME'])

    command = input(">_")
    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command in directions:
        try:
            room_name = current_node["PATHS"][command]
            current_node = world_map[room_name]
        except KeyError:
            print("I can't Go that Way")
    else:
        print("Command Not recognized.")
