
import time

class Test:
    def __init__(self, text):
        self.text = text
        self.user_input = ""
        self.start_time = 0
        self.end_time = 0

    def start_test(self):
        # print(self.text)
        self.start_time = time.time()
        self.user_input = input("Start Typing: \n")
        self.end_time = time.time()

    def calculate_wpm(self):
        total_time = self.end_time - self.start_time

        word_count = len(self.user_input.split())
        wpm = (word_count / total_time) * 60

        return round(wpm, 2)
