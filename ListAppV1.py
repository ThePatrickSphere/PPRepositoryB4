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
8. Sort list
9. Remove from list
10. Print list
11. Quit program""")
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
                removeNumber()
            elif choice == "10":
                printLists()
            else:
                break
            
        except:
             print("You made a mistake! Try again.")
"""
addToList()
The function adds individual numbers to the list by
asking for user input and then appending the list with the integer.
"""
def addToList():
    print("Adding to a list...")
    newItem = input("Type an integer here.")
    myList.append(int(newItem))
"""
addABunch()
This function adds multiple numbers at a time by asking for user input for
2 things: how many numbers to add, and the maximum range of these numbers.
Then the for loop appends the list with random numbers ranging from 0 to the
"how high" input until the "how much" input is reached.
"""
def addABunch():
    print("Adding a bunch of integers here...")
    numberToAdd = input("How many integers would you like to add?   ")
    numberRange = input("And how high would you like these numbers to go?   ")
    for x in range(0, int(numberToAdd)):
        myList.append(random.randint(0, int(numberRange)))
    print("Your list is now complete! Type 10 to see list.")
"""
indexValues()
This one searches for what number is at a given index position.
When the user inputs an index value, the print statement prints the number in the specific index value.
"""
def indexValues():
    print ("Getting a particular piece of data...")
    indexPos = input("What index position are you curious about?     ")
    print(myList[int(indexPos)])
"""
sortList(myList)
This function adds to the list unique_list through a for loop that
appends unique numbers to it if not already there.
The unique_list is then sorted numerically. The input asks the user if they want to see the unique_list.
"""
def sortList(myList):
    print("Sorting your list...")
    for x in myList:
        if x not in unique_list:
            unique_list.append(x)
    unique_list.sort()
    showMe = input("Do you want to see your new list?  Y/N")
    if showMe.lower() == "y":
        print(unique_list)
"""
randomSearch()
This function prints a random number in the list through returning
the value stored at a random index position in range.
"""
def randomSearch():
    print("Randomly searching...")
    print(myList[random.randint(0, len(myList)-1)])
    if len(unique_list) > 0:
        print(unique_list[random.randint(0, len(unique_list)-1)])
"""
linearSearch()
The function here looks through the list one number
at a time until it finds the input term the user is looking for.
It then prints the index position that search term is located at.
"""
def linearSearch():
    print("Checking out each item one at a time in your list...")
    searchItem = input("What're you lookin' for?     ")
    for x in range(len(myList)):
        if myList[x] == int(searchItem):
            print("Your item is at index position {}".format(x))
"""
recursiveBinarySearch(unique_list, low, high, x)
This searches through the unique list through repeating a process of
dividing the list in two. It assigns certain numbers low, mid, and high
until the search term is found in the mid position.
"""
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
"""
iterativeBinarySearch(unique_list, x)
This is similar to recursive binary search in that it
searches for the midpoint in a list to return the search term.
But the function here keeps the midpoint the same and adds or subtracts
the low and high points until the search term is the mid point.
"""
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
"""
removeNumber()
This self-created function removes numbers through the list depending on the
contents of each list. If the unique list is empty, the function removes a
number from myList. If not, it will remove numbers from both lists
and print which one was removed.
"""
def removeNumber():
    print("Deleting a number...")
    deleteItem = input("Which number would you like to remove?    ")
    if len(unique_list) == 0:
        myList.remove(int(deleteItem))
        print(myList)
    else:
        unique_list.remove(int(deleteItem))
        myList.remove(int(deleteItem))
        print(unique_list)
    print("The number {} was removed from your list!".format(deleteItem))
"""
printLists()
This prints lists depending on the length of the unique_list. If empty, myList
will be printed automatically. If not, the function will ask the user
to print either the sorted list (unique_list) or the unsorted list(myList).
"""
def printLists():
    if len(unique_list) == 0:
        print(myList)
    else:
        whichOne = input("Which list? Sorted or unsorted?   ")
        if whichOne.lower() == "sorted":
            print(unique_list)
        else:
            print(myList)
        
"""
This is the "dunder name, dunder main" statement that calls the main program
into action if it were to run as a standalone app.
"""
if __name__ == "__main__":
    mainProgram()
