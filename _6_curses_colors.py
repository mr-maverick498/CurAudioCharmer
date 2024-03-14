import curses

# initialising curses
stdscr = curses.initscr()
curses.cbreak()
curses.noecho()
stdscr.keypad(True)

# for using color we use curses.start_color() for color initialization
# curses.has_color() can be used before start_color to check if terminal support the colors or not.
if curses.has_color(): curses.start_color()

# restoring terminal
curses.nocbreak()
curses.echo()
stdscr.keypad(False)

curses.endwin()