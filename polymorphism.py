class English:
    def greet(self):
        return "Hello"

class Polish:
    def greet(self):
        return "dzien Dobry"

def make_greeting(greeting):
    print(greeting.greet())
make_greeting(English())
make_greeting(Polish())