#!usr/bin/python3.6
#pylint: disable=C0116:missing-function-docstring,C0115:missing-class-docstring,C0103:invalid-name,C0114:missing-module-docstring
import curses


class UI:
    def __init__(self):
        self.stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        self.stdscr.keypad(True)
        curses.start_color()
        curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)


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

    def mainloop(self):
        pass


if __name__=="__main__":
    ui = UI()
    ui.addstr("Hello There!")
    inp = ui.getinput("Please provide input\nOver here: ")
    ui.addstr("\n"+inp)
    ui.stdscr.getkey()
    ui.kill()
