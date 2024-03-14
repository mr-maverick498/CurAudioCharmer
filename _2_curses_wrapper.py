import curses

def main(stdscr) -> None:
    # add the str "HELLO, WORLD!" in the window stdscr at position (y=3, x=3) with REVERSE VIDEO ATTRIBUTE
    stdscr.addstr(3, 3, "HELLO, WORLD!", curses.A_REVERSE)
    # Update the virtual screen and physical screen
    stdscr.refresh()
    # Creates a 1 sec or 1000ms delay
    curses.napms(1000)

    stdscr.addstr(3, 3, "HELLO, !DLROW", curses.A_UNDERLINE)
    stdscr.refresh()
    curses.napms(1000)

    c1 = stdscr.getch(0, 0)
    # refreshes the screen and then waits for the user to hit a key, displaying the key if echo() has been called earlier. 
    # You can optionally specify a coordinate to which the cursor should be moved before pausing.
    # getch will return the value between 0 to 255 for all ascii character
    #  Values greater than 255 are special keys such as Page Up, Home, or the cursor keys. You can compare the value returned to constants such as curses.KEY_PPAGE, curses.KEY_HOME, or curses.KEY_LEFT

    c2 = stdscr.getkey()
    # does the same thing as getch() but converts the integer to a string.
    # Individual characters are returned as 1-character strings, and special keys such as function keys return longer strings containing a key name such as KEY_UP or ^G
    print(c1, c2)

if __name__ == "__main__":
    # wrapper function will initialize the standard_screen and call cbreak(), noecho() and initialize color if possible
    # it takes a callable object and runs it.
    # when the callable returns it restore the terminal state successfully and if anr error occured returns the traceback of exception
    # otherwise some times error can cause the terminal to be in unresponsive state
    curses.wrapper(main)