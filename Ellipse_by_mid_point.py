from graphics import *
import time
def midptellipse(rx, ry, xc, yc):
    x = 0;
    y = ry;
    win = GraphWin('Midpoint Ellipse', 600, 500)
    print("\n\nCoordinates")
    # Initial decision parameter of region 1
    d1 = ((ry * ry)-(rx * rx * ry) +(0.25 * rx * rx))
    dx = 2 * ry * ry * x;
    dy = 2 * rx * rx * y;
    while (dx < dy):
        print("(", x + xc, ",", y + yc, ")")
        win.plotPixel( x + xc,y + yc,"blue")
        
        print("(",-x + xc,",", y + yc, ")")
        win.plotPixel( -x + xc,y + yc,"blue")
        
        print("(",x + xc,",", -y + yc ,")")
        win.plotPixel( x + xc,-y + yc,"blue")
        
        print("(",-x + xc, ",", -y + yc, ")")
        win.plotPixel( -x + xc,-y + yc,"blue")
        
        if (d1 < 0):
           x += 1
           dx = dx + (2 * ry * ry)
           d1 = d1 + dx + (ry * ry)
        else:
           x += 1
           y -= 1
           dx = dx + (2 * ry * ry)
           dy = dy - (2 * rx * rx)
           d1 = d1 + dx - dy + (ry * ry)
           d2 = (((ry * ry) * ((x + 0.5) * (x + 0.5))) + ((rx * rx) * ((y - 1) * (y - 1))) - (rx * rx * ry * ry))
    while (y >= 0):
            print("(", x + xc, ",", y + yc, ")")
            win.plotPixel( x + xc,y + yc,"blue")
            
            print("(", -x + xc, ",", y + yc, ")")
            win.plotPixel( -x + xc,y + yc,"blue")
            
            print("(", x + xc, ",", -y + yc, ")")
            win.plotPixel( x + xc,-y + yc,"blue")
            
            print("(", -x + xc, ",", -y + yc, ")")
            win.plotPixel( -x + xc,-y + yc,"blue")
            
            if (d2 > 0):
               y -= 1
               dy = dy-(2 * rx * rx)
               d2 = d2 + (rx * rx)-dy
            else:
               y -= 1
               x += 1
               dx = dx + (2 * ry * ry)
               dy = dy-(2 * rx * rx)
               d2 = d2 + dx-dy + (rx * rx)
def main():
    rx = int(input("Enter radius along X Coordinate: "))
    ry = int(input("Enter radius along Y Coordinate: "))
    xc = int(input("Enter center of X Coordinate: "))
    yc = int(input("Enter center of Y Coordinate: "))
    midptellipse(rx, ry, xc, yc)

if __name__ == "__main__":
    main()
