import math

x = float(input("输入x的值: "))

#Method 01
if x >= 0:
    y = (x*x-3*x)/(x+1) + 2*math.pi + math.sin(x)
if x < 0:
    y = math.log(-5*x) + 6*math.sqrt(math.fabs(x)+(math.e)**4) - (x-1)**3
print(f"方法一: x = {x:.2f}, y = {y}")

#Method 02
if x >= 0:
    y = (x*x-3*x)/(x+1) + 2*math.pi + math.sin(x)
else:
    y = math.log(-5*x) + 6*math.sqrt(math.fabs(x)+(math.e)**4) - (x-1)**3
print(f"方法二: x = {x:.2f}, y = {y}")

#Method 03
if x >= 0:
    y = (x*x-3*x)/(x+1) + 2*math.pi + math.sin(x)
elif x < 0:
    y = math.log(-5*x) + 6*math.sqrt(math.fabs(x)+(math.e)**4) - (x-1)**3
print(f"方法三: x = {x:.2f}, y = {y}")

#Method 04
y = (x*x-3*x)/(x+1) + 2*math.pi + math.sin(x) if x >= 0 else math.log(-5*x) + 6*math.sqrt(math.fabs(x)+(math.e)**4) - (x-1)**3
print(f"方法四: x = {x:.2f}, y = {y}")