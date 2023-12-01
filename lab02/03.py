#Method 1
print("方法1:")
count = 0
for year in range(2000, 3001):
    if not(year % 4) and year % 100 or not (year % 400):
        print(year, end='   ')
        count+=1
        if count == 15:
            print()
            count = 0

#Method 2
print("\n\n方法2:")
year = 2000
count = 0
while(year <= 3000):
    if not(year % 100):
        if not(year % 400):
            print(year, end='   ')
            count+=1
    else:
        print(year, end='   ')
        count+=1
    if count == 15:
        print()
        count = 0
    year += 4