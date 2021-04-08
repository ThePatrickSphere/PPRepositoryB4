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
3. Return a value at an index position
4. Random search
5. Linear search
6. Recursive binary search
7. Iterative binary search
8. Sort List
9. Print list
10. Quit program""")
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
                searchItem = input("What number are you looking for?   ")
                recursiveBinarySearch(unique_list, 0, len(unique_list)-1, int(searchItem))
            elif choice == "7":
                searchItem = input("What number are you looking for?   ")
                result = iterativeBinarySearch(unique_list, int(searchItem))
                if result != -1:
                    print("Your number is at index {}".format(result))
                else:
                    print("Your number is not found in that list!")
            elif choice == "8":
                sortList(myList)
            elif choice == "9":
                printLists()
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
    print("Your list is now complete! Type 9 to see list.")

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
    if len(unique_list) > 0:
        print(unique_list[random.randint(0, len(unique_list)-1)])

def linearSearch():
    print("Checking out each item one at a time in your list...")
    searchItem = input("What're you lookin' for?     ")
    for x in range(len(myList)):
        if myList[x] == int(searchItem):
            print("Your item is at index position {}".format(x))

def recursiveBinarySearch(unique_list, low, high, x):
    if high >= low:
        mid = (high + low) // 2

        if unique_list[mid] == x:
            print("Your number is found at index position {}".format(mid))
            return mid
        elif unique_list[mid] > x:
            return recursiveBinarySearch(unique_list, low, mid - 1, x)
        else:
            return recursiveBinarySearch(unique_list, mid + 1, high, x)
    else:
        print("Your number isn't here.")

def iterativeBinarySearch(unique_list, x):
    low = 0
    high = len(unique_list)-1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        if unique_list[mid] < x:
            low = mid + 1
        elif unique_list[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

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
