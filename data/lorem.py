from lorem_text import lorem

class Lorem:
    def __init__(self):
        self.lorem = lorem

    def generate_words(self, num_words):
        return self.lorem.words(num_words)

    def print_words(self, words):
        print(words)
