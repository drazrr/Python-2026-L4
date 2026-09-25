import math
x1 = float(input("Enter your x1 :"))
y1 = float(input("Enter your y1 :"))
x2 = float(input("Enter your x2 :"))
y2 = float(input("Enter your y2 :"))
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
print(distance)
