#!usr/bin/python3.6
#pylint: disable=C0116:missing-function-docstring,C0115:missing-class-docstring,C0103:invalid-name,C0114:missing-module-docstring
import curses
from dataclasses import dataclass

MENUCOLORS = 2
SELECTEDCOLORS = 3

@dataclass
class Menu:
    title: str
    options :list
    bindings :list


class UI:
    def __init__(self):
        self.stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        self.stdscr.keypad(True)
        curses.start_color()
        curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
        curses.init_pair(MENUCOLORS, curses.COLOR_BLACK, curses.COLOR_YELLOW)
        curses.init_pair(SELECTEDCOLORS, curses.COLOR_YELLOW, curses.COLOR_BLACK)


    def kill(self):
        curses.nocbreak()
        self.stdscr.keypad(False)
        curses.echo()
        curses.endwin()

    def addstr(self, string: str, x: int  = None, y: int = None, color_pair: int = 0):
        if x is None:
            x = self.stdscr.getyx()[1]
        if y is None:
            y = self.stdscr.getyx()[0]
        try:
            self.stdscr.addstr(y, x, string, curses.color_pair(color_pair))
            self.stdscr.refresh()
        except curses.error:
            self.kill()

    def getinput(self, prompt:str = None):
        y = self.stdscr.getyx()[0]
        self.stdscr.move(y+1, 0)
        if prompt is not None:
            self.addstr(prompt)
        y,x = self.stdscr.getyx()
        rtrn = ""
        while True:
            key = self.stdscr.getkey()
            if str(key) in ("KEY_ENTER", "\n", "\r"):
                break
            if str(key) in ("KEY_BACKSPACE", "\b", "\x7f") :
                rtrn = rtrn[:-1]
            if len(str(key))==1:
                rtrn+=str(key)
            self.stdscr.move(y, x)
            self.stdscr.clrtoeol()
            self.addstr(rtrn)
        return rtrn
    
    def handle_menu(self, menu:Menu):
        curses.curs_set(0)
        eols = []
        pointer = 0
        self.addstr("\n"+menu.title, None, None, MENUCOLORS)
        for option in menu.options:
            y, x = self.stdscr.getyx()
            self.stdscr.move(y+1, 0)
            self.addstr("  "+option)
            eols.append((y+1,x))
        while True:
            self.stdscr.move(eols[pointer][0], eols[pointer][1])
            for i, option in enumerate(menu.options):
                self.stdscr.move(eols[i][0], 0)
                self.stdscr.clrtoeol()
                if i == pointer:
                    self.addstr("  "+option, None, None, SELECTEDCOLORS)
                else:
                    self.addstr("  "+option)
            self.stdscr.move(eols[pointer][0], eols[pointer][1])
            c = self.stdscr.getkey()
            if str(c) == "KEY_UP":
                pointer = (pointer-1)%len(menu.options)
            if str(c) == "KEY_DOWN":
                pointer = (pointer+1)%len(menu.options)
            if str(c) in ("KEY_ENTER", "\n", "\r"):
                menu.bindings[pointer]()
            if str(c) in ("KEY_BACKSPACE", "\b", "\x7f") :
                break
        curses.curs_set(1)


if __name__=="__main__":
    ui = UI()
    ui.addstr("Hello There!")
    def foo1():
        ui.addstr("bar1", 0, 10)
    def foo2():
        ui.addstr("bar2", 0, 10)
    def foo3():
        ui.addstr("bar3", 0, 10)
    menu1 = Menu("Menu#1", ["beep", "flash", "kill"], [foo1, foo2, foo3])
    ui.handle_menu(menu1)
    ui.stdscr.getkey()
    ui.kill()
