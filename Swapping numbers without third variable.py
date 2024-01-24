#Swapping two numbers without using third variable

first = int(input("Enter first number : "))
second = int(input("Enter second number : "))
print("Numbers before swapping : ",first,second)

# Swapping logic
first, second = second, first
print("Numbers after swapping : ",first,second)