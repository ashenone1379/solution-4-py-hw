#! /usr/bin/python

#hw1-1输出水仙花数
def narcissistic_number():
    print("The narcissistic numbers in [100, 1000) are:")
    for num in range(100, 1000):
        ones = num % 10
        tens = num // 10 % 10
        hundreds = num // 100
        if ones**3 + tens**3 + hundreds**3 == num:
            print(num, end=' ')
    print()

narcissistic_number()



#hw1-2选择法排序设计        
def select_sort(nums:list = [1, 1, 4, 5, 1, 4], nonincrease = False) -> list:
    length = len(nums)
    for i in range(length-1):
        min = nums[i]
        flag = i
        for j in range(i+1, length):
            if nums[j] < min:
                flag = j
                min = nums[j]
        nums[i], nums[flag] = nums[flag], nums[i]
    if nonincrease:
        nums.reverse()
    print(nums)
    return nums

select_sort()

#hw1-3因式分解
def factorization(num = 60):
    print(num, ' = ', end='')
    i = 2
    while i < num:
        if num % i:
            i += 1
        else:
            print(i, '* ', end='')
            num //= i
    print(i)

factorization()
