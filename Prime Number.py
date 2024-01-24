# Prime Number Function
# Example : 2,3,5,7,11,13...
num = int(input("Enter the number : "))

def prime(num):
    if num < 2:
        return(False)
    elif num == 2:
        return(True)
    else:
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return(False)
        else:
            return(True)

print(prime(num))
 