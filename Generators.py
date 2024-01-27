#Generators

def even(n):
    for i in range(n):
        if i % 2 == 0:
            yield i 

for i in even(12):
    print(i)