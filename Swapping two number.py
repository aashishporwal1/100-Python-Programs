# Swapping two numbers using third variable

first = int(input("Enter first number : "))
second = int(input("Enter second number : "))
print("Numbers before swapping : ",first,second)

#swapping logic
temp = first
first, second = second, temp
print("Numbers after swapping : ",first,second)