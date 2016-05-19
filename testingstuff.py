largest = None
smallest = None

while True:
    number = raw_input("Enter a number or enter 'done' to stop the script: ")
    if number == "done" : break
    try:
        num = float(inp)
    except:
        print "Please enter only numbers! You can also enter 'done' to stop the script"
        continue
    if smallest is None:
        smallest = num
    if num > largest :
        largest = num
    elif num < smallest :
        smallest = num

def done(largest,smallest):
    print "Maximum is", int(largest)
    print "Minimum is", int(smallest)

done(largest,smallest)





