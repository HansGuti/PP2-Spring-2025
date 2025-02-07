class Dialog:
    def __init__(self):
        self.stinge = ''
    def getString(self):
        self.stinge = input('Enter a string: ')

    def printString(self):
        print(self.stinge.upper())

obj = Dialog()
obj.getString()
obj.printString()