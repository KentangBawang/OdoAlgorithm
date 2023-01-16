import math
import intoPos
count = 0
xFix = 0
yFix = 0
theta =0
theta_temp = 0
theta_state = 0

xTarget = 10
yTarget = 10

theta = int(input("masukan sudut orientasi : "))
    
rad = math.radians(theta)
pulse = int(input("masukan pulse : "))
jarak = pulse/15
print(jarak)
x = jarak*math.cos(rad)
y = jarak*math.sin(rad)
xTemp =x
yTemp =y

xFix = xTemp+x
yFix = yTemp+y
print("x :",xFix)
print("y :",yFix)





theta = int(input("masukan sudut orientasi : "))
    
rad = math.radians(theta)
pulse = int(input("masukan pulse : "))
jarak = pulse/15
print(jarak)
x = jarak*math.cos(rad)
y = jarak*math.sin(rad)
xFix = xTemp+x
yFix = yTemp+y

print("x :",xFix)
print("y :",yFix)


theta = int(input("masukan sudut orientasi : "))
    
rad = math.radians(theta)
pulse = int(input("masukan pulse : "))
jarak = pulse/15
print(jarak)
x = jarak*math.cos(rad)
y = jarak*math.sin(rad)
xFix = xTemp+x
yFix = yTemp+y

print("x :",xFix)
print("y :",yFix)

intoPos.getPos(xFix, yFix)


