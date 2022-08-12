#program to find all prime numbers up to a given range of numbers

start = int(input("enter the starting range"))
end = int(input("enter the end range"))
print("prime number in range", start, "to", end)
for i in range(start, end+1):
    flag = 0
    for j in range(2, i):
        if (i % j == 0):
            flag = 1
            break
    if (flag == 0):
        print(i, end = ' ')


