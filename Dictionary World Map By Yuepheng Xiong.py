world_map = {
    'R19A': {
        'NAME': "Mr. Wiebe's Room",
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
    }
}
