from data.lorem import Lorem
from typing_test.test import Test

import curses
import time

def run_test(stdscr):
    curses.curs_set(1)
    stdscr.clear()
    stdscr.addstr(2, 2, "Enter the number of words to generate: ")
    stdscr.refresh()

    num_words = get_num_input(stdscr)
    return num_words

def get_num_input(stdscr):
    curses.echo()
    num_str = ""

    while True:
        key = stdscr.getch()

        """
        curses uses ASCII values for characters.
        https://www.cs.cmu.edu/~pattis/15-1XX/common/handouts/ascii.html
        """

        if key == 10: # 10 is enter in ASCII
            break
        elif key == 127:
            num_str = num_str[:-1]
        elif chr(key).isdigit():
            num_str += chr(key)

        stdscr.addstr(2, 34, num_str)
        stdscr.refresh()

    curses.noecho()
    return int(num_str) if num_str.isdigit() else 10 # Use 10 as default here if misentered or no val



def main():

    num_words = curses.wrapper(run_test)

    lorem = Lorem()
    generated_words = lorem.generate_words(num_words)

    test = Test(generated_words)

    lorem.print_words(generated_words)
    test.start_test()

    # print(f'Your starting time was: {test.start_time}')
    # print(f'Your ending time was: {test.end_time}')
    print(f'Your words per minute was: {test.calculate_wpm()}')



if __name__ == "__main__":
    main()
