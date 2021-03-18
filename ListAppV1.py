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
2. Add a bunch of numbers
3. Return a value at an index
4. Random search
5. Print contents of list
6. Exit program""")
            if choice == "1":
                addToList()
            elif choice == "2":
                addABunch()
            elif choice == "3":
                indexValues()
            elif choice == "4":
                randomSearch()
            elif choice == "5":
                print(myList)
            else:
                break
            
        except:
             print("You made an mistake!")

def addToList():
    print("Adding to a list...")
    newItem = input("Type an integer here.")
    myList.append(int(newItem))

def addABunch():
    print("Adding a bunch of integers here...")
    numberToAdd = input("How many integers would you like to add?   ")
    numberRange = input("And how high would you like these numbers to go?   ")
    for x in range(0, int(numberToAdd)):
        myList.append(random.randint(0, int(numberRange)))
    print("Your list is now complete!")

def indexValues():
    print ("Getting a particular piece of data...")
    indexPos = input("What index position are you curious about?     ")
    print(myList [int(indexPos)])

def randomSearch():
    print("Randomly searching...")
    print(myList[random.randint(0, len(myList)-1)])

def linearSearch():
    print("Checking out each item one at a time in your list...")
    searchItem = input("What're you lookin' for?     ")
    for x in range(len(myList)):
        if myList[x] == int(searchItem):
            print("Your item is at index position {}".format(x))

if __name__ == "__main__":
    mainProgram()
