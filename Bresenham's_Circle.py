from graphics import *
import time
def Bresenham_Circle(x_cordinate,y_cordinate,radius):
    d=3-2*radius
    x=0
    y=radius
    win = GraphWin('Brasenham Circle', 600, 500)
    print("\n\nCoordinates")
    while x<=y:
        print(x_cordinate+x,y+y_cordinate)
        win.plotPixel(x_cordinate+x,y+y_cordinate,"red")
        
        print(x_cordinate-y,y_cordinate-x)
        win.plotPixel(x_cordinate-y,y_cordinate-x,"red")

        print(x_cordinate+y,y_cordinate-x)
        win.plotPixel(x_cordinate+y,y_cordinate-x,"red")

        print(x_cordinate-y,y_cordinate+x)
        win.plotPixel(x_cordinate-y,y_cordinate+x,"red")

        print(x_cordinate+y,y_cordinate+x)
        win.plotPixel(x_cordinate+y,y_cordinate+x,"red")

        print(x_cordinate-x,y_cordinate-y)
        win.plotPixel(x_cordinate-x,y_cordinate-y,"red")

        print(x_cordinate+x,y_cordinate-y)
        win.plotPixel(x_cordinate+x,y_cordinate-y,"red")

        print(x_cordinate-x,y_cordinate+y)
        win.plotPixel(x_cordinate-x,y_cordinate+y,"red")

        if d<0:
            d=d+4*x+6
        else:
            d=d+4*x-4*y+10
            y=y-1
        x=x+1   
        
def main():
    x = int(input("Enter X Coordinate: "))
    y = int(input("Enter Y Coordinate: "))
    r = int(input("Enter Radius: "))
    Bresenham_Circle(x,y,r)            

if __name__ == "__main__":
    main()        
