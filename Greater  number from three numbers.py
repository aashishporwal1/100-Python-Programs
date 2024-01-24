first = int(input("Enter first number : "))
second = int(input("Enter second number : "))
third = int(input("Enter third number : "))

if first > second:
    if first > third:
        print(first," is greater")
    else:
        print(third," is greater")
    
else:
    print(third," is greater")
