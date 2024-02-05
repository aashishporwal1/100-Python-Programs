# Program to locate a number (say 'card') from a list or bunch of cards.

cards = [1,1,2,2,3,4,5,6,7,8,9]
query = int(input("Enter the number you want to find :"))
def locateCards(cards, query):
    '''
    ~ Program for Binary Search.
    ~ The input list must be sorted.
    '''
    
    lowest, highest = 0, len(cards) - 1

    while lowest <= highest:
        mid = (lowest + highest) // 2
        mid_number = cards[mid]

        print("Lowest :",lowest, "Highest :",highest,"Mid :",mid,"Mid number :",mid_number)

        if mid_number == query:
            return  mid
        elif mid_number > query:
            highest = mid - 1
        elif mid_number < query:
            lowest = mid + 1
    return "Number not found."

print(locateCards(cards,query))