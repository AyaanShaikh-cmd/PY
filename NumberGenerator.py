from random import Random

Random()

def IamUnique():
    """
    Generates a unique number between 1 and 1000.
    """
    return Random().randint(1, 1000)

if __name__=="__main__":
    numbers = IamUnique()
    for number in numbers:
        print(number)
    
