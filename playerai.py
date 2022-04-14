#!usr/bin/Python3
from ast import parse
from glob import iglob
import random
from tracemalloc import start
import generator
import re

SHOT = re.compile(r"([A-Z])\s*([0-9]+)\s*")
COLUMNS = "ABCDEFGHIJ"
OUTCOMES = {
    "m": -1,
    "h": 1,
    "s": 2,
    -1: "miss",
    1: "hit",
    2: "sunk"
    }

def parse_shot(shot:str):
    s = SHOT.match(shot)
    row = int(s.group(2))-1
    column = COLUMNS.find(s.group(1))
    return (row, column)


class PlayerAI:
    def __init__(self):
        self.my_board = generator.Board()
        self.enemy = [
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
        self.ships_sunk = 0
        self.options = [(x, y) for x in range(10) for y in range(10)]
        self.queue = []

    def get_result(self, shot:tuple):
        print(COLUMNS[shot[1]], shot[0]+1)
        result = input("miss, hit or sunk?m/h/s: ")
        while not result in ["m", "h", "s"]:
            result = input("invalid outcome!\nm/h/s?")
        return OUTCOMES[result]

    def mark_sunken(self, pos:tuple, previous:tuple = None):
        x, y = pos
        neighbours = []
        if x>0:
            neighbours.append((x-1, y))
        if x<9:
            neighbours.append((x+1, y))
        if y>0:
            neighbours.append((x, y-1))
        if y<9:
            neighbours.append((x, y+1))
        for neigh in neighbours:
            if self.enemy[neigh[1]][neigh[0]]== 1 and neigh!=previous:
                self.mark_sunken(neigh, pos)
        #fixme: marks the wrong tiles with 2s, need to check it dry
        for i in [-1, 0, 1]:
            if y+i>9 or y+i<0:
                continue
            for j in [-1, 0, 1]:
                if x+j<0 or x+j>9:
                    continue
                self.enemy[y+i][x+j] = 2
        for option in self.options:
            if self.enemy[option[1]][option[0]] == 2:
                self.options.remove(option)
        

    def handle_result(self, pos:tuple, result:int):
        x, y = pos
        if result == -1:
            return
        elif result == 1:
            self.enemy[y][x] = 1
            if x>0:
                to_append = (x-1, y)
                if to_append in self.options:
                    self.queue.append(to_append)
                    self.options.remove(to_append)
            if x<9:
                to_append = (x+1, y)
                if to_append in self.options:
                    self.queue.append(to_append)
                    self.options.remove(to_append)
            if y>0:
                to_append = (x, y-1)
                if to_append in self.options:
                    self.queue.append(to_append)
                    self.options.remove(to_append)
            if y<9:
                to_append = (x, y+1)
                if to_append in self.options:
                    self.queue.append(to_append)
                    self.options.remove(to_append)
        elif result == 2:
            self.queue = []
            self.ships_sunk+=1
            self.mark_sunken(pos)
        
    def recieve_shot(self, pos:tuple):
        if self.my_board.get_cell(pos) == 0:
            return -1
        self.my_board.set_cell(pos, 2)
        for ship in self.my_board.taken_spaces:
            for space in ship:
                if space[0] == pos[0] and space[1] == pos[1]:
                    ship.remove(space)
                    if len(ship) == 0:
                        return 2
                    return 1

    def play(self):
        self.my_board.fill()
        starting = random.randint(0, 1)
        if(starting == 0):
            print("I BEGIN")
        else:
            print("YOU BEGIN")
        print("GIVE ANY INPUT WHEN READY")
        input()
        round = 0
        #fixme: problems with detecting when the game has ended
        while self.my_board.is_any_afloat and self.ships_sunk < 10:
            if round%2 == starting:#when it's bots turn
                if len(self.queue) == 0:
                    shot = self.options.pop(random.randrange(0, len(self.options)))

                else:
                    shot = self.queue.pop(random.randrange(0, len(self.queue)))
                res = self.get_result(shot)
                self.handle_result(shot, res)
                if res == -1:
                    round +=1
            else:#when it's players turn
                shot = input().upper()
                while not SHOT.match(shot):
                    shot = input().upper()
                shot = parse_shot(shot)
                res = self.recieve_shot(shot)
                print(OUTCOMES[res])
                if res == -1:
                    round+=1
        if self.ships_sunk<10:
            print("YOU WON!")
            return
        print("YOU LOST!")

if __name__ == "__main__":
    player = PlayerAI()
    player.play()