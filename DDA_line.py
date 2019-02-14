#DDA line
from graphics import *
import time
def ROUND(a):
	return int(a + 0.5)

def drawDDA(x1,y1,x2,y2):
	x,y = x1,y1
	length = (x2-x1) if (x2-x1) > (y2-y1) else (y2-y1)
	dx = (x2-x1)/float(length)
	dy = (y2-y1)/float(length)
	#print ('x = %s, y = %s' % (((ROUND(x),ROUND(x)))))
	win = GraphWin('DDA', 600, 480)
	PutPixle(win, ROUND(x),ROUND(x))
	for i in range(length):
		x += dx
		y += dy
		#print ('x = %s, y = %s' % (((ROUND(x),ROUND(y)))))
		time.sleep(0.01)
		PutPixle(win, ROUND(x),ROUND(x))


def PutPixle(win, x, y):
    """ Plot A Pixle In The Windows At Point (x, y) """
    pt = Point(x,y)
    pt.draw(win)
  
def main():
    x1 = int(input("Enter Start X1: "))
    y1 = int(input("Enter Start Y1: "))
    x2 = int(input("Enter End X2: "))
    y2 = int(input("Enter End Y2: "))
    drawDDA(x1,y1,x2,y2)
if __name__ == "__main__":
    main()    
         
