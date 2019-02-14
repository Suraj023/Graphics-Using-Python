# midPoint function for line generation
from graphics import *
import time
def midPoint(X1,Y1,X2,Y2):  
    # calculate dx & dy  
    dx = X2 - X1  
    dy = Y2 - Y1  
  
    # initial value of decision parameter d  
    d = dy - (dx/2)  
    x = X1 
    y = Y1  
    win = GraphWin('Mid_Point Line', 600, 480)
    win.setBackground("36")
    print(Text(Point(3,4), "Hello!"))
    PutPixle(win, x, y)
    print(x,",",y,"\n") 
    # iterate through value of X  
    while (x < X2): 
        x=x+1
        # E or East is chosen 
        if(d < 0): 
            d = d + dy  
  
        # NE or North East is chosen  
        else: 
            d = d + (dy - dx)  
            y=y+1
      
  
        # Plot intermediate points  
        # putpixel(x,y) is used to print pixel  
        # of line in graphics
        time.sleep(0.1)
        PutPixle(win, x, y)
        print(x,",",y,"\n")  
      
def PutPixle(win, x, y):
    """ Plot A Pixle In The Windows At Point (x, y) """
    pt = Point(x,y)
    pt.draw(win)    
  
if __name__=='__main__': 
    x1 = int(input("Enter Start X1: "))
    y1 = int(input("Enter Start Y1: "))
    x2 = int(input("Enter End X2: "))
    y2 = int(input("Enter End Y2: "))
    midPoint(x1, y1, x2, y2) 
