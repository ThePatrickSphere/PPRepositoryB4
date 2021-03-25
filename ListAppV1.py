import random
myList = []
unique_list = []
def mainProgram():
    while True:
        try:
            print("Hello, there! Let's work with some lists!")
            print("Choose one of the following options. Type a number below.")
            choice = input("""1. Add to a list
2. Add a bunch of numbers
3. Return a value at an index
4. Random search
5. Linear search
6. Print contents of list
7. Exit program""")
            if choice == "1":
                addToList()
            elif choice == "2":
                addABunch()
            elif choice == "3":
                indexValues()
            elif choice == "4":
                randomSearch()
            elif choice == "5":
                linearSearch()
            elif choice == "6":
                sortList(myList)
            else:
                break
            
        except:
             print("You made a mistake! Try again.")

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
    print("Your list is now complete! Type 6 to see list.")

def indexValues():
    print ("Getting a particular piece of data...")
    indexPos = input("What index position are you curious about?     ")
    print(myList[int(indexPos)])

def sortList(myList):
    print("Sorting your list...")
    for x in myList:
        if x not in unique_list:
            unique_list.append(x)
    unique_list.sort()
    showMe = input("Do you want to see your new list?  Y/N")
    if showMe.lower() == "y":
        print(unique_list)

def randomSearch():
    print("Randomly searching...")
    print(myList[random.randint(0, len(myList)-1)])

def linearSearch():
    print("Checking out each item one at a time in your list...")
    searchItem = input("What're you lookin' for?     ")
    for x in range(len(myList)):
        if myList[x] == int(searchItem):
            print("Your item is at index position {}".format(x))

def printLists():
    if len(unique_list) == 0:
        print(myList)
    else:
        whichOne = input("Which list? Sorted or unsorted?   ")
        if whichOne.lower() == "sorted":
            print(unique_list)
        else:
            print(myList)
        

if __name__ == "__main__":
    mainProgram()
