Guide to the Ultimate List-Creating App

Software Instructions

Inititate the program and type a whole number ranging from 1 to 10. These numbers represent options such as 
adding to a list of numbers, searching the list, sorting the list, or other actions. 
There are two lists in this program: one named "sorted" for unique user-inputted numbers in numerical order, and one named "unsorted" for any user-inputted numbers in no particular order. The list of unique numbers will only be available if you choose to sort the list of numbers.
If you type 11 or any higher number, the program will quit. 
Please do not type any float (number with a decimal point) or non-number in an input to select an option or interact with the list, as the program does not recognize these inputs.

Option 1: Adding a number
When prompted, add 1 integer of your choice to the input field.

Option 2: Adding multiple numbers
When prompted, type an integer representing the amount of numbers you would like to add to the list. Then type the highest possible value you would like the numbers to be. Type 10 to print the list. Please keep in mind that although the program accepts extremely high amounts of numbers, inserting that will most likely cause the system to crash.

Option 3: Searching an index position
When prompted, Type a number ranging from 0 to the length of the list. This number is the list's index position. The integer value stored at that position will be returned to you. Numbers out of range will cause the function not to work.

Option 4: Random search
If you type the number 4 in the option list, a random number in the list will be returned to you. You must type 4 to initiate the random search.

Option 5: Linear search
When prompted, type a number in the list you wish to search for. If that number is in the list, the index position will be returned to you. If not, the program will continue and the program will not alert you.

Options 6 and 7: Recursive and Iterative binary search
When prompted, type a number in the list you wish to search for. If that number is in the list, the index position will be returned to you. If not, the program will alert you of the absence of the number.

Option 8: Sorting list
If you type the number 8 in the option list, the algorithm will add unique numbers to the "sorted" list and sort numbers in numerical order. If you would like to see the sorted list, type "y"; if not, type "n". Do not type any other character into the input.

Option 9: Removing from list
When prompted, type a number from either list you wish to remove. The system will print the new list with the requested integer removed. Typing a number not present in your list will result in error.

Option 10: Printing list(s)
If prompted to select a list, type alphabetically which list you want printed. Type "sorted" to see the sorted list. Type "unsorted" to see the unsorted list. If you type any other word, the unsorted list will be printed.


Binary Search

In this program, there are 2 options for binary search: recursive and iterative. Although both search functions produce the same result when a number is searched for,  the functions have different ways of going about it.
Binary search is the act of calling the program to search for numbers in a binary way, like yes and no, or true and false. When a program runs, it assign numbers the values low, mid, and high. Then it goes through the intended search item and compares it to the middle value. 
If the search item is the middle, the program will return the middle point; if the search item is less than middle, it will only focus on numbers from low to mid; if the search item is greater than middle it will focus on numbers mid to high.
However, this complex system has limitations and requirements in order to work. The set of numbers must be in numerical order, which is why this function only works for the sorted list. Also, the process can be work-heavy for computers and may cause the system not to work up to speed. Other than that it's a legit algorithm.

In recursive binary search, the algorithm repeats a procedure in which the list is cut down from one side or the other until the mid point is the target value. 
For example, if the target is 12 and the mid is 5, the system will disregard all numbers below mid and assign new low, mid, and high values to numbers above it. 
Mid is determined by the equation (low + high) / 2, while new high and low values during recursion are determined by adding 1 to or subtracting 1 from mid. 
This procedure repeats itself in a conditional statement until the middle value matches the target value. The system then prints which index position this is located at if the number is present in the list.

In iterative binary search, the algorithm enacts a specific procedure once. Rather than removing numbers above or below mid, iterative search trims the low and high values from the set of numbers until mid is the target value. 
If the target number is 24 and mid is 54, the system will snip and reassign the low and high values until they produce the solution to the equation (low + high) / 2. 
This function runs in a while loop, as it runs through a process of trimming numbers once until the midpoint is reached. The system then returns the target's index position in the same way.


Recommendations for Change

While the list-making app is a good basic tool for creating sets of numbers, it can very well be improved upon. In my opinion, the program has a lot to do with searching for what is already in the list and not editing lists further. 
I would adapt the program to have more options for iterating the number list available. One implementation I have made in my program is a function to delete individual numbers from the list. 
When prompted, the user may strike a number from the list through the basic "remove" action and it will print the list and specify which number was removed. 
The code segment is written as such: 

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

If the sorted list is empty, the system will remove a number from the unsorted list and present it without the deleted number. This function only deletes one occurrence of the number. 
If the user notices that there are more occurrences, they can use the remove option again to delete the number until it is no longer in the list.
But if the list is sorted, then the program will remove the number from both the sorted and unsorted lists. 
With the sorted lists, any number occurs one time, to one deletion is all that's needed. But the number may still exist in the unsorted list if multiple occurrences were not deleted before.
No program can be perfect, but one that expands beyond the expectations of normal interaction with a program can be a brilliant invention, even if it is as basic as this "ultimate" list-creating app.