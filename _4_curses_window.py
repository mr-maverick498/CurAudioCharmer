import curses

# initialising curses
stdscr = curses.initscr()
curses.cbreak()
curses.noecho()
stdscr.keypad(True)

#  curses.newwin(nlines, ncols, begin_y, begin_x)
# Return a new window, whose left-upper corner is at (begin_y, begin_x), and whose height/width is nlines/ncols.
#  By default, the window will extend from the specified position to the lower right corner of the screen.
# if ncols or nlines is given as zero then extend upto the maximum lines or max. cols
# parameter must be 2 or 4
my_win = curses.newwin(0, 3)
my_win.box("|", '-')
my_win1 = curses.newwin(0, 3, 0, 4)
my_win1.box()
my_win2 = curses.newwin(3, 0, 0, 8)
my_win2.box()
my_win3 = curses.newwin(3, 0, 4, 8)
my_win3.box()

my_win.refresh()
my_win1.refresh()
my_win2.refresh()
my_win3.refresh()
curses.napms(2000)

# restoring terminal
curses.nocbreak()
curses.echo()
stdscr.keypad(False)

curses.endwin()