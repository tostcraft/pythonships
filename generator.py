#!usr/bin/Python3
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
    
    def check_place(self, origin:list, ship:list):
        x = origin[0]
        y = origin[1]
        if x>0:
            x-=1
        if y>0:
            y-=1
        for i in range(len(ship)+origin[1]-y+1):
            if y+i>9:
                break
            for j in range(len(ship[0])+origin[0]-x+1):
                if x+j>9:
                    break
                if self.content[y+i][x+j] == 1:
                    return False
        return True

    def fill(self, rules: list):
        for type in range(len(rules)):
            q = rules[type] #q for quantity
            for i in range(q):
                ship = random.choice(SHIPS[type])
                pointer = [random.randint(0, 10-len(ship[0])), random.randint(0, 10-len(ship))]
                while not self.check_place(pointer, ship):
                    pointer = [random.randint(0, 10-len(ship[0])), random.randint(0, 10-len(ship))]
                for row in ship:
                    for element in row:
                        self.content[pointer[1]][pointer[0]] = element
                        pointer[0]+=1
                    pointer[1]+=1
                    pointer[0]-=len(row)
    
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


board = Board()
board.fill([4, 3, 2, 1])
print(str(board))