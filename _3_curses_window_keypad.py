import curses

stdscr = curses.initscr()
curses.cbreak()
# curses.noecho()
# stdscr.keypad(True)

print("WITHOUT KEYPAD TRUE")
# if keypad is set to False then it will not process special keys like KEY_UP, KEY_DOWN, etc. and just ignore them 
c = stdscr.getch(0, 0)
print(c)

c = stdscr.getkey(1, 2)
print(c)

c = stdscr.getstr(2, 2)
print(c)

print("\nWITH KEYPAD AS TRUE")
## Now with keypad set as TRUE
stdscr.keypad(True)

c = stdscr.getch(3, 3)
print(c)

c = stdscr.getkey(4, 4)
print(c)

c = stdscr.getstr(5, 5)
print(c)

curses.echo()
curses.nocbreak()
stdscr.keypad(False)
curses.endwin()