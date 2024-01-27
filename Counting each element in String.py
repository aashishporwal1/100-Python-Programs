#Counting each element in string irrespective of case.

str = input("Enter the string :")
elements = {}
for i in str.casefold():
    if i in elements:
        elements[i] += 1
    else:
        if i == " ":
            continue
        else:
            elements[i] = 1

print(elements)