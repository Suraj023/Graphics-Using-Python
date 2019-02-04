from graphics import *

def BresenhamLine(x1,y1,x2,y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    slope = dy/float(dx)
    x, y = x1, y1   
 
    # creating the window
    win = GraphWin('Brasenham Line', 600, 500)
    
    # checking the slope if slope > 1 
    # then interchange the x and y
    if slope > 1:
        dx, dy = dy, dx
        x, y = y, x
        x1, y1 = y1, x1
        x2, y2 = y2, x2
 
    # initialization of the inital disision parameter
    p = 2 * dy - dx
    
    #PutPixle(win, x, y)
    win.plotPixel(x,y,"lightblue")
    print("\n\nCoordinates")
    print("(",x,",",y,")")
 
    for k in range(2, dx+2):
        if p > 0:
            y = y + 1 if y < y2 else y - 1
            p = p + 2*(dy - dx)
        else:
            p = p + 2*dy
 
        x = x + 1 if x < x2 else x - 1
        time.sleep(0.1)
        win.plotPixel(x,y,"lightblue")
        print("(",x,",",y,")")

def main():
    x1 = int(input("Enter Start X1: "))
    y1 = int(input("Enter Start Y1: "))
    x2 = int(input("Enter End X2: "))
    y2 = int(input("Enter End Y2: "))
    BresenhamLine(x1,y1,x2,y2)
        
if __name__ == "__main__":
    main()
