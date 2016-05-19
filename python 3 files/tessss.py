largest = None
smallest = None

while True:
    number = raw_input("Enter a number or enter 'done' to stop the script: ")
    if number == "done":
        break
    try:
        number = float(number)
        if smallest is None:
            smallest = number
        elif number < smallest:
            smallest = number
        if number > largest:
            largest = number
    except:
        print "Please enter only numbers! You can also enter 'done' to stop the script"
        continue
print "the smallest and largest are:"
print smallest
print largest

import sys
print sys.version