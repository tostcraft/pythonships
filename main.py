#!/usr/bin/python3.6
#pylint: disable=C0116:missing-function-docstring,C0115:missing-class-docstring,C0103:invalid-name,C0114:missing-module-docstring
import random
import re

from src import playerai
from src import uihandler

ERR1 = (1001, "Given coordinates appear to be out of range!")
HIT = 2
SUNK = -1
MISS = 0
EXIT = "0000"

SHOT = re.compile(r"([A-Z])\s*([0-9]+)\s*")
COLUMNS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
OUTCOMES = {
    "m": MISS,
    "h": HIT,
    "s": SUNK,
    MISS: "MISS",
    HIT: "HIT",
    SUNK: "SUNK"
    }

def parse_shot(shot: str):
    s = SHOT.match(shot)
    if s is None:
        return 0
    row = int(s.group(2))-1
    column = COLUMNS.find(s.group(1))
    return (column, row)


class Game:
    def __init__(self):
        self.ui = uihandler.UI()
        self.player = playerai.PlayerAI()
        self.main_menu = uihandler.Menu(
            "Main Menu",
            ("Play", "Options", "Exit"),
            (self.start_game, self.enter_options, self.end_process)
        )
        self.ui.handle_menu(self.main_menu)

    def start_game(self):
        self.ui.stdscr.clear()
        self.ui.stdscr.move(0, 0)
        self.mainloop()

    def reset(self):
        self.ui.stdscr.clear()
        self.ui.stdscr.move(0, 0)
        self.ui.handle_menu(self.main_menu)

    def enter_options(self):
        pass

    def end_process(self):
        self.ui.kill()

    def fill_ai_board(self):
        retry = self.player.my_board.fill()
        while retry:
            retry = self.player.my_board.fill()


    def get_result(self, shot: tuple):
        self.ui.addstr("\n"+COLUMNS[shot[0]]+str(shot[1]+1))
        result = self.ui.getinput("miss, hit or sunk?m/h/s: ")
        while result not in ("m", "h", "s"):
            result = self.ui.getinput("invalid outcome!\nm/h/s?: ")
        return OUTCOMES[result]

    def mainloop(self):
        self.fill_ai_board()
        starting = random.randint(0, 1)
        if starting == 0:
            self.ui.addstr("I BEGIN\n")
        else:
            self.ui.addstr("YOU BEGIN")
        round_no = 0
        
        while len(self.player.my_board.taken_spaces)>0 and self.player.ships_sunk<10:
            y, x = self.ui.stdscr.getyx()
            try:
                self.ui.stdscr.move(y+1, x)
                self.ui.stdscr.move(y, x)
            except uihandler.curses.error:
                self.ui.stdscr.clear()
                self.ui.stdscr.move(0, 0)
            if round_no%2 == starting: #when it's bots turn
                shot = self.player.choose_shot()
                res = self.get_result(shot)
                self.player.handle_result(shot, res)
                if res == MISS:
                    round_no+=1
            else: #when it's humans turn
                shot = self.ui.getinput(">>").upper()
                if shot == EXIT:
                    break
                shot = parse_shot(shot)
                while not shot:
                    shot = parse_shot(shot)
                res = self.player.recieve_shot(shot)
                if res == ERR1:
                    self.ui.addstr("\n"+res[1])
                    continue
                self.ui.addstr("\n"+OUTCOMES[res])
                if res == MISS:
                    round_no+=1
        self.ui.addstr("\nThank you for playing, provide input in order to exit!")
        self.ui.stdscr.getkey()
        self.reset()


if __name__ == "__main__":
    game = Game()
