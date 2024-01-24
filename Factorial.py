# Factorial of a number
# Example : Factorial of 5 = 1*2*3*4*5 = 120

num = int(input("Enter the number : "))
factorial = 1
for i in range(1,num+1):
    factorial *= i
print(factorial)
