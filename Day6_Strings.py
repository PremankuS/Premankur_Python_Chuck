#looking inside strings

fruit = "banana"
letter = fruit [2]
print letter

#built in funktion len

print len(fruit)

#looping through strings; indefitie loop

index = 0

while index < len(fruit):
    letter = fruit [index]
    print index, letter
    index=index+1
    print index

#definite loop

for letter in fruit:
    print letter

#counting the 'a' in banana
count = 0

for letter in fruit:
    if letter == "a":
        count = count +1
    print count

#slicing using the colon

string = "Monty Python"
print string[0:5]
print string[:]
print string[6:]

#what is our string made up of?
boolean = "n" in string
print boolean

if "n" in string:
    print("found n")


word = raw_input("Please enter your word:")
if word < "banana":
    print "hallo"

#string library

new_string = "Hallo, Bob "
new_string_lower = new_string.lower ()
print new_string_lower

directory = dir(new_string)
print directory

pos = new_string.find("Bo")
print pos

helios= new_string.strip()
print helios



