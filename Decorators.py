#Decorators 

def makePretty(func):
    def inner():
        print("Decorated function.")
        func()
    return inner

@makePretty
def ordinary():
    print("Ordinary function.")
ordinary()