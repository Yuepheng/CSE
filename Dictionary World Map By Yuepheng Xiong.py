world_map = {
    'R19A': {
        'NAME': "Mr. Wade's Room",
        'DESCRIPTION': "THis is the room you are in",
        'PATHS': {
            'NORTH': "PARKING_LOT",
            'WEST': "AMPHITHEATER",
            'EAST': "R13B"

        }

    },
    'PARKING_LOT': {
        'NAME': "A Parking Lot",
        'DESCRIPTION': "THere are a few cars parked here",
        'PATHS': {
            'WEST': 'R19A',
            'NORTH': 'DOWNTOWN DRESNO'
        }
    },
    'AMPHITHEATER': {
        'NAME': "The Stage outside",
        'DESCRIPTION': "There might be some items here",
        'PATHS': {
            'NORTH': 'R19A',
            'SOUTH': 'CAFETERIA'
        }
    },
    'CAFETERIA': {
        'NAME': "The place to get food and chill",
        'DESCRIPTION': "There is some leftover non eaten ham and cheese bars and there might"
                       "be some items here",
        'PATHS': {
            'SOUTH': 'AMPHITHEATER',
            'NORTH': 'SB20'
        }
    },
    'SB20': {
        'NAME': "Mr. Yang's Room",
        'DESCRIPTION': "This guy loves Anime",
        'PATHS': {
            'EAST': 'CAFETERIA',
            'SOUTH': 'PARKING_LOT',
        }
    },
    'DOWNTOWN DRESNO': {
        'NAME': "The City of Dresno",
        'DESCRIPTION': "There are a lot of work offices here",
        'PATHS': {
            'SOUTH': 'ETHAN JAMES HIGH SCHOOL',
            'EAST': 'GRANDPARENTS HOUSE',
            'SOUTHEAST': 'PARENTS HOUSE',
            'NORTH': 'SAN FRAMCISCO',
            'NORTHEAST': 'J MART'
        }
    },
    'ETHAN JAMES HIGH SCHOOL': {
        'NAME': "ETHAN JAMES HIGH SCHOOL GRADE 9-12",
        'DESCRIPTION': "The School",
        'PATHS': {
            'NORTH': "DOWNTOWN DRESNO",
            'WEST': "OFFICE"
        }
    },
    'GRANDPARENTS HOUSE': {
        'NAME': "My grandparents live here along with some aunties and uncles",
        'DESCRIPTION': "There could be some items here",
        'PATHS': {
            'SOUTHWEST': "DOWNTOWN DRESNO",
            'SOUTHEAST': "PARENTS HOUSE",

        }
    },
    'PARENTS HOUSE': {
        'NAME': "My Mom, Dad, 2 sisters and brother live here",
        'DESCRIPTION': "There could be some helpful items here",
        'PATHS': {
            'SOUTHWEST': "GRANDPARENTS HOUSE",
            'SOUTHEAST': "COUSINS HOUSE"
        }
    },
    'OFFICE': {
        'NAME': "The Front desk of Ethan James high school",
        'DESCRIPTION': "You could talk to the VPs, assistants, and staff",
        'PATHS': {
            'SOUTH': "R19A",
            'WEST': "PARKING_LOT",
            'NORTH': "DOWNTOWN DRESNO"
        }
    },
    'SAN FRAMSICO': {
        'NAME': "THE CITY OF THE RICH PEOPLE",
        'DESCRIPTION': "I might need some items in the stores here",
        'PATHS': {
            'SOUTH': "DOWNTOWN DRESNO"
        }
    },
    'COUSINS HOUSE': {
        'NAME': "My Cousins live here",
        'DESCRIPTION': "They might be of help to me",
        'PATHS': {
            'NORTH': "PARENTS HOUSE",
        }
    },
    'R13B': {
        'NAME': "Mr. Dawson's Room",
        'DESCRIPTION': "There could be some useful items here",
        'PATHS': {
            'NORTH': "R19A",
            'SOUTH': "CAFETERIA",
            'EAST': "SL15"
        }
    },
    'SL15': {
        'NAME': "Mrs. Hazen's Biology Room",
        'DESCRIPTION': "There might be some useful items here",
        'PATHS': {
            "NORTH": "R19A",
            "SOUTH": "CAFETERIA"
        }
    },
    'J MART': {
        'NAMES': "The J Mart to get food, technology, clothing etc",
        'DESCRIPTION': "I might need some of the useful items here",
        'PATHS': {
            "WEST": "DOWNTOWN DRESNO"
        }
    },
}


# Other Variables
directions = ["SOUTHEAST", "SOUTHWEST", "NORTH", "SOUTH", "EAST", "WEST", "UP"]
current_node = world_map["R19A"]  # THis is your current location
playing = True

# Controller
while playing:
    print(current_node['NAME'])
    print(current_node['DESCRIPTION'])
    print(current_node['PATHS'])

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
