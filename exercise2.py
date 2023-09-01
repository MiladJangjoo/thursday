class Coding():
    def __init__(self):
        self.userInput = None
    def get_String(self):
        self.userInput = input('What is your name? ')
    def print_String(self):
        print(self.userInput.upper())

milad = Coding()
milad.get_String()
milad.print_String()