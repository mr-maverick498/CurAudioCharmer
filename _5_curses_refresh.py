import curses

# initialising curses
stdscr = curses.initscr()
curses.cbreak()
curses.noecho()
stdscr.keypad(True)

# window.noutrefresh() method can be used to update an underlying data structure representing the desired state of the window.
# doupdate() function to change the physical screen to match the desired state recorded in the data structure.
# refresh calls noutrefresh() and doupdate() both 
# therefore to reduce screen flicker noutrefresh() can be called for each window and call curses.doupdate() once to refresh physical screen
my_win = curses.newwin(0, 3)
my_win.box()
my_win.noutrefresh()
curses.napms(2000)
# output will not be visible until getkey call is instantiated because no doupdate() call is not given to refresh physical screen
my_win.addch("K", curses.A_REVERSE)
my_win.getkey()

## for doupdate()
my_win1 = curses.newwin(0, 3, 0, 3)
my_win1.box()
my_win1.noutrefresh()
curses.doupdate()
curses.napms(4000)
# to verify if box is drawn before this character printing
my_win1.addch("A", curses.A_REVERSE)
my_win1.getkey()

# restoring terminal
curses.nocbreak()
curses.echo()
stdscr.keypad(False)

curses.endwin()