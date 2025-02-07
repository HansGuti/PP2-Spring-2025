class Shape:
    def area(self):
        return 0
class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length
    
length = int(input('Enter the length of a square: '))
square = Square(length)
print(f'Area of a square is: {square.area()}')      