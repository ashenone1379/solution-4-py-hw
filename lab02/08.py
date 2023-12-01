from math import sqrt

a = float(input("请输入系数a:"))
b = float(input("请输入系数b:"))
c = float(input("请输入系数c:"))

delta = b*b - 4*a*c
if a == 0:
    if b == 0:
        print("此方程无解!")
    else:
        print(f"此方程解为{-c/b:.2f}")
elif delta == 0:
    print(f"此方程有两个相等的实根: {-b/(2*a)}")
elif delta > 0:
    print(f"此方程有两个不等的实根: {-b/(2*a)+sqrt(b*b-4*a*c)/(2*a)}和{-b/(2*a)-sqrt(b*b-4*a*c)/(2*a)}")
else:
    print(f"此方程有两个共轭复根: {-b/(2*a)}+{sqrt(4*a*c-b*b)/(2*a)}i 和{-b/(2*a)}-{sqrt(4*a*c-b*b)/(2*a)}i")