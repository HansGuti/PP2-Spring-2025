class Shape:
    def area(self):
        return 0
class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2
    
square = Square(int(input('Enter the length of the square: ')))
print(f'Area of a square is: {square.area()}')      