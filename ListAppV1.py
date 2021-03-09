"""
Program Goals:
1. Get input from user (at multiple points)
2. Convert some input to INT from STR
3. Provide choices to user
    a. Add more avalues to list
    b. Return value at specific index

"""

def mainProgram():
    myList = []
    print("Hello, there! Let's work the some lists!")
    print("Choose one of the following options. Type a number below.")
    choice = input("1. Add to list, 2. Return value at an index position.  ")
    if choice == "1":
        addToList()
    elif choice == "2":
        indexValues()
    # To Add: 1. A way to loop action, 2. A loop to quit, 3. Repetition

def addToList():
    print("Adding to a list...")
    newItem = input("Type an integer here.")
    myList.append(int(newItem))

def indexValues():

if __name__ == "__main__":
    mainProgram()
