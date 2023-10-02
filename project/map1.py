map_ = [
    [
        [
            {'name': 'Wardrobe', 'upstairs': 0, 'downstairs': 0, 'description': 'Wardrobe'},
            {'name': 'Bathroom', 'upstairs': 0, 'downstairs': 0, 'description': 'Bath'},
            {'name': 'Room', 'upstairs': 0, 'downstairs': 0, 'description': 'You\'re in the gloomy muggy room. '
                                            'The creaky floor and shabby furniture'}
        ],
        [
            {'name': 'Hallway', 'upstairs': 0, 'downstairs': 0, 'description': 'Hallway'},
            {'name': 'Hallway', 'upstairs': 1, 'downstairs': 0, 'description': 'Hallway'},
            {'name': 'Hall', 'upstairs': 1, 'downstairs': 0, 'description': 'Hall'},
            {'name': 'Garden', 'upstairs': 0, 'downstairs': 0, 'description': 'You\'re in the roses garden. '
                                              'Such a fresh and balmy air!'}
        ],
        [
            {'name': 'Kitchen', 'upstairs': 0, 'downstairs': 0, 'description': 'Kitchen'},
            {'name': 'Dining room', 'upstairs': 1, 'downstairs': 0, 'description': 'Dining room'},
            {'name': 'Living room', 'upstairs': 0, 'downstairs': 0, 'description': 'You\'re in the Living room'}
        ]
    ],
    [
        [
            {'name': 'Bedroom', 'upstairs': 0, 'downstairs': 0, 'description': 'Bedroom'},
            {'name': 'Bathroom', 'upstairs': 0, 'downstairs': 0, 'description': 'Bath'},
            {'name': 'Room', 'upstairs': 0, 'downstairs': 0, 'description': 'You\'re in the gloomy muggy room. '
                                                           'The creaky floor and shabby furniture'}
        ],
        [
            {'name': 'Room', 'upstairs': 0, 'downstairs': 0, 'description': 'Room'},
            {'name': 'Space', 'upstairs': 0, 'downstairs': 1, 'description': 'Space'},
            {'name': 'Library', 'upstairs': 0, 'downstairs': 1, 'description': 'Library'},
            {'name': 'Sunroom', 'upstairs': 0, 'downstairs': 0, 'description': 'The roses garden is underneath'}
        ],
        [
            {'name': 'Bathroom', 'upstairs': 0, 'downstairs': 0, 'description': 'Bathroom'},
            {'name': 'Living room', 'upstairs': 0, 'downstairs': 1, 'description': 'You\'re in the Living room'},
            {'name': 'Office', 'upstairs': 0, 'downstairs': 0, 'description': 'Office'}
        ]
    ]
]

if __name__ == '__main__':
    for i in range(len(map_)):
        for j in range(len(map_[i])):
            print('{:^20}'.format(map_[i][j]['name']), end='|')
        print()

    print(map_[0][2][2]['name'])

'''
      Wardrobe      |      Bathroom      |        Room        |
      Hallway       |      Hallway       |        Hall        |       Garden       |
      Kitchen       |    Dining room     |    Living room     |

       Bedroom      |      Bathroom      |        Room        |
       Room         |      Space         |       Library      |       Sunroom       |
       Bathroom     |    Living room     |       Office       |
'''