while True:
    score = raw_input("Enter Score: ")
    score=float(score)
    if score > 1.0:
        print ("out of range. try again")
    elif score < 0.0:
        print ("out of range. try again")
    elif score >= 0.9:
        print ("A")
    elif score >= 0.8:
        print ("B")
    elif score >= 0.7:
        print ("C")
    elif score >= 0.6:
        print ("D")
    elif score < 0.6:
        print ("F")
    continue



#def prog1():
    #print ("hello world")

#prog1()

big=("hello world")

big1=max(big)

print(big1)