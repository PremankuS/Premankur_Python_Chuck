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
