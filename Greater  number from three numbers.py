first = int(input("Enter first number : "))
second = int(input("Enter second number : "))
third = int(input("Enter third number : "))

largest = first
if second > largest:
    largest = second
if third > largest:
    largest = third

print("Largest number is :",largest)