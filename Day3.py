#conditional statements. if statement asks a question. if this then that

x=5
if x<10:
    print("Smaller")
if x>10:
    print("Bigger")

print("finis")

#conditional operators

x=6
if x>=5:
    print("hello")
if x==5:
    print("Halleluja")
else : print("smaller")
# dont goddamn forget ==.
x=3
if x==2:
    print("hallo1")
elif x>2:
    print("hallo2")
else:
    print("hallo3")
print("hallo world")

# multiway puzzles.

x=4
try:
    if x>5:
        print("above 5")
    elif x==5:
        print("below 5")
except:
    print ("hello world")

#excercise

# Method 1:

hours=float(input("Enter the hours: "))
rate=float(input("Enter the rate: "))

if hours>=40:
    payday=float(hours)*float(rate)*1.5
    print ("salary", payday)
else:
    hours<40
    payday=float(hours)*float(rate)
    print ("salary", payday)


# Method 2 using just if und else --WORKING

hours=input("Enter the hours: ")
rate=input("Enter the rate: ")
if hours>=40:
    payday = float(hours) * float(rate) * 1.5
    print ("salary", payday)
else:
    payday = float(hours) * float(rate)
    print ("salary", payday)



