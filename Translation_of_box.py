from graphics import *
import time
def translation_of_Box(x1,y1,x2,y2,x3,y3,x4,y4,tx,ty):
    win = GraphWin('Translation', 600, 480)
    R = [[0, 0, 0,0], 
	 [0, 0, 0,0], 
	 [0, 0, 0,0]] 

    
    t=[[tx,0,0],
       [0,ty,0],
       [0,0,1]]
    
    p=[[x1,x2,x3,x4],
       [y1,y2,y3,y4],
       [1,1,1,1]]
    
    for i in range(0,3):
        for j in range(0,4):
          for k in range(0,3):
            R[i][j]+=t[i][k]*p[k][j]
            
    for i in range(0,3): 
	    for j in range(0,4): 
		    print(R[i][j],end=" ") 
	    print("\n",end="")
	    
if __name__=='__main__': 
    x1 = int(input("Enter Start X1: "))
    y1 = int(input("Enter Start Y1: "))
    x2 = int(input("Enter End X2: "))
    y2 = int(input("Enter End Y2: "))
    x3 = int(input("Enter Start X3: "))
    y3 = int(input("Enter Start Y3: "))
    x4 = int(input("Enter Start X4: "))
    y4 = int(input("Enter Start Y4: "))
    tx = int(input("Enter Start tx: "))
    ty = int(input("Enter Start ty: "))
    translation_of_Box(x1,y1,x2,y2,x3,y3,x4,y4,tx,ty)	
