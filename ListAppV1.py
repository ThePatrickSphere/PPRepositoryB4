"""
Program Goals:
1. Get input from user (at multiple points)
2. Convert some input to INT from STR
3. Provide choices to user
    a. Add more avalues to list
    b. Return value at specific index

"""
myList = []
def mainProgram():
    while True:
        print("Hello, there! Let's work the some lists!")
        print("Choose one of the following options. Type a number below.")
        choice = input(""" 1. Add to a list or
2. Reurn a value at an index
3. Exit program""")
        if choice == "1":
            addToList()
        elif choice == "2":
            indexValues()
        elif choice == "3":
            break
        # To Add: 1. A way to loop action, 2. A loop to quit, 3. Repetition

def addToList():
    print("Adding to a list...")
    newItem = input("Type an integer here.")
    myList.append(int(newItem))

def indexValues():
    print ("Getting a particular piece of data...")
    indexPos = input("What index position are you curious about?     ")
    print(myList [int(indexPos)])

if __name__ == "__main__":
    mainProgram()
