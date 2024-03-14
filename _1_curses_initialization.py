import curses

# for initializing internal data structure for manipulating terminal screen
# it sends required codes to terminal
terminal_screen = curses.initscr()

# disable automatic echo of input character 
curses.noecho()

# disable the line bufferring of input, it means input keys are processed without needing to press enter 
# special sequence like control keys retain their effect
curses.cbreak()

# keypad(True) means special keys like PAGE_UP as multi byte sequences is automatically processed
terminal_screen.keypad(True)

# only defined after initscr() is called
# legal cordinates are (0, 0) to (curses.LINES - 1, curses.COLS - 1)
# curses.LINES -> returns the height or maximum no. of rows terminal has
# curses.COLS -> returns the width of terminal in character count or maximum columns a terminal can accomodate
print("LINES/ROWS : ", curses.LINES, "\nCOLUMNS/WIDTH : ", curses.COLS)

## for ending the curses program

# enable automatic echo of input
curses.echo()

# change to cooked mode or enable line buffering of input 
curses.nocbreak()

# De-initialize curses library
curses.endwin()