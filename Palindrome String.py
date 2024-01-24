# Palindrome String
# Example : "DAD"

word = input("Enter the string to be checked : ")
rev = ''

for i in word[::-1]:
    rev = rev + i

print("Is Palindrome") if rev == word else  print("Is not Palindrome")