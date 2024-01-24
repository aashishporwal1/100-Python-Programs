#Fibonacci Sequence
# 0 1 1 2 3 5 8 13 ....

first, second = 0, 1
n = int(input("Enter no. of elements you want: " ))
print(first)
print(second)
i = 1
while i < (n-1):
    sum = first + second
    first, second = second, sum
    print(sum)
    i += 1