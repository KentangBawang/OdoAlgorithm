import math
xTarget = 10
yTarget = 10

def getPos(xNow,yNow):
    xGo = xTarget-xNow
    yGo = yTarget-yNow
    sudut = math.atan2(yGo, xGo)
    sudutGo = sudut*(180/math.pi)
    jarak = math.sqrt(xGo*xGo+yGo*yGo)

    print("X :",xGo,"Y : ",yGo,"Sudut : ",sudutGo, "Jarak : ", jarak)
