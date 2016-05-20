# using a loop to start the converter right after it finishes coverting

def converter_algorithm (score):
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

while True:
    score = raw_input("Enter Score: ")
    if score == "done":
        break
    try:
        score = float(score)
        converter_algorithm(score)
        continue
    except ValueError:
        print ("Put in your grade please!")

