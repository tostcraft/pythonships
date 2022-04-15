#!usr/bin/Python3
#pylint: disable=C0116:missing-function-docstring,C0115:missing-class-docstring,C0103:invalid-name,C0114:missing-module-docstring
import re
import random

import generator

HIT = 2
SUNK = -1
MISS = 0


SHOT = re.compile(r"([A-Z])\s*([0-9]+)\s*")
COLUMNS = "ABCDEFGHIJ"
OUTCOMES = {
    "m": MISS,
    "h": HIT,
    "s": SUNK,
    MISS: "miss",
    HIT: "hit",
    SUNK: "sunk"
    }

def parse_shot(shot: str):
    s = SHOT.match(shot)
    row = int(s.group(2))-1
    column = COLUMNS.find(s.group(1))
    return (column, row)


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

    @staticmethod
    def get_result(shot: tuple):
        print(COLUMNS[shot[0]], shot[1]+1)
        result = input("miss, hit or sunk?m/h/s: ")
        while not result in ["m", "h", "s"]:
            result = input("invalid outcome!\nm/h/s?")
        return OUTCOMES[result]

    def mark_sunk(self, pos: tuple, previous: tuple = None):
        x, y = pos
        neighbours = []
        if x > 0:
            neighbours.append((x-1, y))
        if x < 9:
            neighbours.append((x+1, y))
        if y > 0:
            neighbours.append((x, y-1))
        if y < 9:
            neighbours.append((x, y+1))
        for neigh in neighbours:
            if self.enemy[neigh[1]][neigh[0]] == HIT and neigh!=previous:
                self.mark_sunk(neigh, pos)
        for i in [-1, 0, 1]:
            if y+i > 9 or y+i < 0:
                continue
            for j in [-1, 0, 1]:
                if x+j < 0 or x+j > 9:
                    continue
                self.enemy[y+i][x+j] = SUNK

    def handle_result(self, pos: tuple, result: int):
        x, y = pos
        if result == MISS:
            return
        if result == HIT:
            self.enemy[y][x] = HIT
            to_append = []
            if x>0:
                to_append.append((x-1, y))
            if x < 9:
                to_append.append((x+1, y))
            if y > 0:
                to_append.append((x, y-1))
            if y < 9:
                to_append.append((x, y+1))
            for option in to_append:
                if option in self.options:
                    self.queue.append(option)
                    self.options.remove(option)

        elif result == SUNK:
            self.queue = []
            self.ships_sunk += 1
            self.mark_sunk(pos)

    def recieve_shot(self, pos: tuple):
        if self.my_board.get_cell(pos) == 0:
            return MISS
        self.my_board.set_cell(pos, HIT)
        for ship in self.my_board.taken_spaces:
            for space in ship:
                if space[0] == pos[0] and space[1] == pos[1]:
                    ship.remove(space)
                    if len(ship) == 0:
                        self.my_board.taken_spaces.remove(ship)
                        return SUNK
                    return HIT

    def play(self, rules:tuple = (4,3,2,1)):
        refill = self.my_board.fill(rules)
        while refill:
            refill = self.my_board.fill(rules)
        starting = 0 #random.randint(0, 1)
        if starting == 0:
            print("I BEGIN")
        else:
            print("YOU BEGIN")
        print("GIVE ANY INPUT WHEN READY")
        input()
        round_no = 0
        while len(self.my_board.taken_spaces)>0 and self.ships_sunk < sum(rules):
            if round_no % 2 == starting:  # when it's bots turn
                if len(self.queue) == 0:
                    shot = self.options.pop(random.randrange(0, len(self.options)))
                else:
                    shot = self.queue.pop(random.randrange(0, len(self.queue)))
                    while self.enemy[shot[1]][shot[0]] == SUNK:
                        shot = self.queue.pop(random.randrange(0, len(self.queue)))
                res = self.get_result(shot)
                self.handle_result(shot, res)
                if res == MISS:
                    round_no += 1

            else:  # when it's players turn
                shot = input().upper()
                while not SHOT.match(shot):
                    shot = input().upper()
                shot = parse_shot(shot)
                res = self.recieve_shot(shot)
                print(OUTCOMES[res])
                if res == MISS:
                    round_no += 1
        if self.ships_sunk < sum(rules):
            print("YOU WON!")
            return
        print("YOU LOST!")


if __name__ == "__main__":
    player = PlayerAI()
    player.play()
