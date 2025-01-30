from data.lorem import Lorem
from typing_test.test import Test
import time

def main():
    num_words = int(input("Enter the number of words to generate: "))

    lorem = Lorem()

    generated_words = lorem.generate_words(num_words)

    test = Test(generated_words)

    countdown = 5
    print('Test will start in:')
    for i in range(5):
        print(countdown)
        countdown -= 1
        time.sleep(1)

    lorem.print_words(generated_words)
    test.start_test()

    # print(f'Your starting time was: {test.start_time}')
    # print(f'Your ending time was: {test.end_time}')
    print(f'Your words per minute was: {test.calculate_wpm()}')



if __name__ == "__main__":
    main()
