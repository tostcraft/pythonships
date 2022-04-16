#!usr/bin/python3.6
#pylint: disable=C0116:missing-function-docstring,C0115:missing-class-docstring,C0103:invalid-name,C0114:missing-module-docstring
import curses
from curses import wrapper

def scr_print(scr: curses.window, string: str):
    scr.addstr(string)

def main(stdscr: curses.window):
    stdscr.clear()


    stdscr.refresh()
    stdscr.getkey()

wrapper(main)
