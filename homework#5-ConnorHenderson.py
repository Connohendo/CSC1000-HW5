# start of Rectangle class
class Rectangle:
    def __init__(self, length, width):  
        self.length = length
        self.width = width
    def GetLength(self):
        return self.length
    def GetWidth(self):
        return self.width
    def GetArea(self):
        return  self.length * self.width
    def SetScale(self, scale):
        self.length = self.length * scale
        self.width = self.width * scale
    def getPerimeter(self):
        self.perimeter = self.length * 2 + self.width * 2
        return self.perimeter
    def isSquare(self):
        if self.length == self.width:
            return True
        else:
            return False

# start of main program

rec = Rectangle(3,5)

rectangleArea = rec.GetArea()

if rec.isSquare() is True:
    print('This is a square.')
else:
    print('This is not a square.')

print ('Rectangle Area: ', rectangleArea)
print('Rectangle perimeter:', rec.getPerimeter())

for  rs  in  range (2,5) :
    width = rec.GetWidth()
    print ('    Current rectangle width:', width)
    rec.SetScale ( rs )
    print ('        Scale factor applied:', rs)  
    width = rec.GetWidth()
    print ('            New rectangle width:', width)
# end of program
# Perimeter function
