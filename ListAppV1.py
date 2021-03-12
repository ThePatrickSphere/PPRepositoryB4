"""
Program Goals:
1. Get input from user (at multiple points)
2. Convert some input to INT from STR
3. Provide choices to user
    a. Add more avalues to list
    b. Return value at specific index

"""
import random
myList = []
def mainProgram():
    while True:
        try:
            print("Hello, there! Let's work with some lists!")
            print("Choose one of the following options. Type a number below.")
            choice = input(""" 1. Add to a list or
2. Return a value at an index
3. Random search
4. Exit program""")
            if choice == "1":
                addToList()
            elif choice == "2":
                indexValues()
            elif choice == "3":
                randomSearch()
            else:
                break
            
        except:
             print("You made an mistake!")

def addToList():
    print("Adding to a list...")
    newItem = input("Type an integer here.")
    myList.append(int(newItem))

def indexValues():
    print ("Getting a particular piece of data...")
    indexPos = input("What index position are you curious about?     ")
    print(myList [int(indexPos)])

def randomSearch():
    print("Randomly searching...")
    print(myList[random.randint(0, len(myList)-1)])

if __name__ == "__main__":
    mainProgram()
