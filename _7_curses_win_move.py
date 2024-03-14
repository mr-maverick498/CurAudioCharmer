import curses
from random import randint as rd

stdscr = curses.initscr()
curses.start_color()
curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLUE)
curses.cbreak()
curses.noecho()
stdscr.keypad(True)

stdscr.box()
curses.doupdate()

mywin = curses.newwin(8, 8, 1, 1)
mywin.border("|", "|", "-", "-", "@", "@", "@", "@")
mywin.addstr("Hellov ")
mywin.bkgdset(" ", curses.color_pair(1))
mywin.refresh()

while True:
    stdscr.clear()
    stdscr.noutrefresh()
    y, x = stdscr.getmaxyx()
    y1, x1 = rd(1, y - 8), rd(1, x - 9)
    mywin.mvwin(y1, x1)
    mywin.border("|", "|", "-", "-", "@", "@", "@", "@")
    mywin.noutrefresh()
    curses.doupdate()
    curses.napms(1000)


curses.endwin()