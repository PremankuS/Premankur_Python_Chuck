hours=raw_input("Please enter your hours:")
rate=raw_input("Please enter your rate:")
try:
    hours=float(hours)
    rate=float(rate)
    if hours>40:
        remhours=hours-40
        payment=((float(hours)-float(remhours))*float(rate))+(float(remhours)*((float(rate)*1.5)))
        print(payment)
    else:
        payment=float(hours)*float(rate)
        print(payment)
except:
    print("Please Use Numeric Input")

astr = 'Hello Bob'
istr = int(astr)
print 'First', istr
astr = '123'
istr = int(astr)
print 'Second', istr

score = raw_input("Enter Score: ")
try:
    if score == 1.0:
        print ("A")
    if score == 0.9:
        print ("A")
    elif score == 0.8:
        print ("B")
    elif score == 0.7:
        print ("C")
    elif score == 0.6:
        print ("D")
    elif score < 0.6:
        print ("F")

except:
    if score>1.0:
        print ("out of range. try again")
