# Palindrome Number

num = int(input("Enter the number : "))
temp = num
reversed = 0
while num > 0:
    digit = num % 10
    reversed = reversed*10 + digit
    num = num // 10

print("Is Palindrome") if reversed == temp else print("Is not Palindrome") 