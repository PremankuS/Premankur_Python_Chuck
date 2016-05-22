n=5
while n>0:
    print n
    n=n-1
print ("Blastoff!")
print n

#iteration variables. some variable that is changing. It controls the numbers. It defines the exit.

#Zero Trip Loop

n=0
while n>0:
    print n
    n=n-1
print ("Blastoff!")
print n

#Breaking out of a loop by "break"

while True:
    line = raw_input(">...")
    if line [0] == "#":
        continue
    if line == ("done"):
        break
    print line
print ("Done!")

#loops with "while" are indefinite loops. Be careful to stop the loop. Notorious source of bug.
# definite loops are with the keyword "for"

for i in [5,4,3,2,1]:
    print i
print ("Blastoff")

bases = ["A","T","G","C"]

for base in bases:
    print "welcome to the Club:",base
print ("Finished")

#for loop decides 2 things: "are we done yet?" and changes the iteration variables as defined.

#LOOP IDIOMS - SMART LOOPS

#finding largest number

largest = None
print (("Before"), largest)
for number in [9,41,42,3,74,15]:
    if largest is None:
        largest = number
    elif number > largest:
        largest = number
    print (largest, number)
print (("After"), largest)


#how to count the number of loops

loop_count = 0
print (("Before"), loop_count)
for number in [9,41,42,3,74,15,34,56,78,45,34,56,99]:
    loop_count=loop_count+1
    print loop_count, number
print (("After"), loop_count)

#summing in a loop

total_sum = 0
print (("Before"), loop_count)
for number in [9,41,42,3,74,15,34,56,78,45,34,56,99]:
    total_sum=total_sum+number
    print total_sum, number
print (("After"), total_sum)

#average of the numbers

loop_count=0
total_sum=0
print (("Before"), loop_count,total_sum)
for number in [9,41,42,3,74,15,34,56,78,45,34,56,99]:
    loop_count = loop_count + 1
    total_sum = total_sum + number
    print loop_count,total_sum,number
print (("After"), (total_sum),loop_count, (total_sum/loop_count))
print (45*13)

#find all the numbers above 70

for number in [9,41,42,3,74,15,34,56,78,45,34,56,99]:
    if number>70:
        print "ooh very large:", number
print "done"

#Boolean variable "True/False"

state=False
print "Before", state
for number in [9,41,42,3,74,15,34,56,78,45,34,56,99]:
    if number == 34:
        state=True
    print(number, state)
print "Done", state

#test_test