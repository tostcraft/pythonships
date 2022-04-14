#!usr/bin/Python3
'''
Generator of random valid boards for a game of battleships
'''
import random


SHIPS = [
    #singles
    [
        [
            [1]
        ]
    ],
    #doubles
    [
        [#horizontal
            [1, 1]
        ],
        [#vertical
            [1],
            [1]
        ]
    ],
    #triples
    [
        [#horizontal
            [1, 1, 1]
        ],
        [#vertical
            [1],
            [1],
            [1]
        ],
        [#L left
            [0, 1],
            [1, 1]
        ],
        [#L left down
            [1, 1],
            [0, 1]
        ],
        [#L right
            [1, 0],
            [1, 1],
        ],
        [#L right down
            [1, 1],
            [1, 0],
        ]
    ],
    #quadruples
    [
        [#horizontal
            [1, 1, 1, 1]
        ],
        [#vertical
            [1],
            [1],
            [1],
            [1]
        ],
        [#3up-right
            [1, 1, 1],
            [0, 0, 1]
        ],
        [#3up-center
            [1, 1, 1],
            [0, 1, 0]
        ],
        [#3up-left
            [1, 1, 1],
            [1, 0, 0]
        ],
        [#3down-right
            [0, 0, 1],
            [1, 1, 1]
        ],
        [#3down-center
            [0, 1, 0],
            [1, 1, 1]
        ],
        [#3down-left
            [1, 0, 0],
            [1, 1, 1]
        ],
        [#3left-down
            [1, 0],
            [1, 0],
            [1, 1]
        ],
        [#3left-center
            [1, 0],
            [1, 1],
            [1, 0]
        ],
        [#3left-up
            [1, 1],
            [1, 0],
            [1, 0]
        ],
        [#3right-down
            [0, 1],
            [0, 1],
            [1, 1]
        ],
        [#3right-center
            [0, 1],
            [1, 1],
            [0, 1]
        ],
        [#3right-up
            [1, 1],
            [0, 1],
            [0, 1]
        ],
        [#square
            [1, 1],
            [1, 1]
        ],
        [#squiggly-left
            [1, 0],
            [1, 1],
            [0, 1]
        ],
        [#squiggly right
            [0, 1],
            [1, 1],
            [1, 0]
        ],
        [#squiggly-up
            [0, 1, 1],
            [1, 1, 0]
        ],
        [#squiggly-down
            [1, 1, 0],
            [0, 1, 1]
        ]

    ]
    ]


class Board():

    def __init__(self):
        self.content = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
        self.taken_spaces = []

    def check_place(self, origin:list, ship:list):
        x, y = origin
        for i, row in enumerate(ship):
            for j, cell in enumerate(row):
                if not cell:
                    continue
                for move_y in [-1, 0, 1]:
                    if y+i+move_y>9 or y+i+move_y<0:
                        continue
                    for move_x in [-1, 0, 1]:
                        if x+j+move_x>9 or x+j+move_x<0:
                            continue
                        if self.content[y+i+move_y][x+j+move_x]==1:
                            return False

        return True

    def reset(self):
        '''
        Restets every board cell to 0.
        '''
        self.content = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]

    def fill(self, rules: tuple = (4, 3, 2, 1)):
        '''
        Generates a random valid board with given ship quantities. In case of failure
        the board will be reset and the process aborted.

        Parameters:
        rules (tuple): the quantities of the 4 types of ships to be placed.
        Must be a 4-element long tuple.
        '''
        assert isinstance(rules, tuple) and len(rules) == 4
        for t, q in enumerate(rules):#t for type, q for quantity
            ships = [random.choice(SHIPS[t]) for x in range(q)]
            for ship in ships:
                pointer = [random.randint(0, 10-len(ship[0])), random.randint(0, 10-len(ship))]
                spaces = []
                tries = 1
                while not self.check_place(pointer, ship) and tries<1000:
                    pointer = [random.randint(0, 10-len(ship[0])), random.randint(0, 10-len(ship))]
                    tries+=1
                if tries == 500:
                    print(f"unable to find a spot for ship: {ship}; board setup failed")
                    self.reset()
                    return -1
                for row in ship:
                    for element in row:
                        self.content[pointer[1]][pointer[0]] = element
                        if element == 1:
                            spaces.append((pointer[0], pointer[1]))
                        pointer[0]+=1
                    pointer[1]+=1
                    pointer[0]-=len(row)
                self.taken_spaces.append(spaces)
        return 0

    def __str__(self):
        rtrn = "~~\n"
        for row in self.content:
            for cell in row:
                if cell==1:
                    rtrn+=" #"
                else:
                    rtrn+=" _"
            rtrn +="\n"
        rtrn+="~~\n"
        return rtrn

    def is_any_afloat(self):
        for row in self.content:
            for cell in row:
                if cell == 1:
                    return True
        return False
    
    def set_cell(self, cell:tuple, value: int):
        self.content[cell[1]][cell[0]] = value

    def get_cell(self, pos:tuple):
        return self.content[pos[1]][pos[0]]

if __name__ == "__main__":
    board = Board()
    board.fill()
    print(str(board))
    print(board.taken_spaces)
