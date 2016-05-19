hours=input("Enter the hours: ")
rate=input("Enter the rate: ")
try:
    hours=float(hours)
    rate=float(rate)
    if  hours>=40:
        payday = float(hours) * float(rate)
        print ("salary", payday)
    else:
        payday = float(hours) * float(rate)
        print ("salary", payday)
except: print ("please use numeric numbers")

print

#40 hours. extra hours 1.5 times the money.

hours=float(input("Please enter your hours:"))
rate=float(input("Please enter your rate:"))
if hours>40:
    remhours=hours-40
    payment=((float(hours)-float(remhours))*float(rate))+(float(remhours)*((float(rate)*1.5)))
    print(payment)
else:
    payment=float(hours)*float(rate)
    print(payment)

# using try, except to make sure that user knows to use numerical inputs
hours=input("Enter the hours: ")
rate=input("Enter the rate: ")
try:
    hours=float(hours)
    rate=float(rate)
    if  hours>=40:
        payday = float(hours) * float(rate)
        print ("salary", payday)
    else:
        payday = float(hours) * float(rate)
        print ("salary", payday)
except: print ("please use numeric numbers")