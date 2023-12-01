from math import sqrt

a = float(input("请输入三角形的边长A: "))
b = float(input("请输入三角形的边长B: "))
c = float(input("请输入三角形的边长C: "))

print(f"三角形三边分别为: a={a:.2f}, b={b:.2f}, c={c:.2f}")

if a <=0 or b <= 0 or c <= 0 or a+b <= c or a+c <= b:
    print("无法构成三角形！")
else:
    l = a + b + c
    h = l/2
    s = sqrt(h*(h-a)*(h-b)*(h-c))

    print(f"三角形边长: {l}, 面积: {s}")