from graphics import *
import time
def midPoint_Circle(x_coordinate,y_coordinate,radius):
    x=radius;y=0
    win = GraphWin('Midpoint Circle', 600, 500)
    print("\n\nCoordinates")
    print(x+x_coordinate,y+y_coordinate)
    win.plotPixel(x+x_coordinate,y+y_coordinate,"blue")
    
    if radius>0:
        print(x+x_coordinate,-y+y_coordinate)
        win.plotPixel(x+x_coordinate,-y+y_coordinate,"red")

        print(y+x_coordinate,x+y_coordinate)
        win.plotPixel(y+x_coordinate,x+y_coordinate,"red")

        print(-y+x_coordinate,x+y_coordinate)
        win.plotPixel(-y+x_coordinate,x+y_coordinate,"red")

    p=1-radius
    while x>y:
        y=y+1
        if p<=0:
            p=p+ 2*y +1
        else:
            x=x-1
            p=p+2*y-2*x+1
        if x<y:
            break
        print(x+x_coordinate,y+y_coordinate)
        win.plotPixel(x+x_coordinate,y+y_coordinate,"blue")

        print(-x+x_coordinate,y+y_coordinate)
        win.plotPixel(-x+x_coordinate,y+y_coordinate,"blue")

        print(x+x_coordinate,-y+y_coordinate)
        win.plotPixel(x+x_coordinate,-y+y_coordinate,"blue")

        print(-x+x_coordinate,-y+y_coordinate)
        win.plotPixel(-x+x_coordinate,-y+y_coordinate,"blue")

        if x!=y:
            print(y+x_coordinate,x+y_coordinate)
            win.plotPixel(y+x_coordinate,x+y_coordinate,"black")

            print(-y+x_coordinate,x+y_coordinate)
            win.plotPixel(-y+x_coordinate,x+y_coordinate,"black")

            print(y+x_coordinate,-x+y_coordinate)
            win.plotPixel(y+x_coordinate,-x+y_coordinate,"black")

            print(-y+x_coordinate,-x+y_coordinate)
            win.plotPixel(-y+x_coordinate,-x+y_coordinate,"black")

def main():
    x = int(input("Enter X Coordinate: "))
    y = int(input("Enter Y Coordinate: "))
    r = int(input("Enter Radius: "))
    midPoint_Circle(x,y,r)            

if __name__ == "__main__":
    main()
