rownum = int(input("输入要显示的行数:"))

row = [0]*(rownum) + [1] + [0]*(rownum)
for i in range(rownum):
    for j in range(2*rownum+1):
        if row[j] == 0:
            print('   ', end='')
        else:
            print(f"{row[j]:3}", end='')
    print()
    row = [0 if k == 0 or k == 2*rownum else row[k-1]+row[k+1] for k in range(2*rownum+1)]