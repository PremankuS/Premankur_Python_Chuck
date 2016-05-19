name = input("Please enter your name:")
hours = input("How many hours did you work?")
rate = input("What was the rate?")

# overtime calculation

def overtime_snippet(hours):
    overtime = float(hours) - 40
    return float(overtime)

#calculation for more than 40 hours work. overtime pays 1.5 times more.

def salcalc_over40(hours, rate):
    s1 = ((float(hours) - overtime_snippet(hours))) * float(rate) + (overtime_snippet(hours) * ((float(rate) * 1.5)))
    return s1

#calculation for  the first 40 hours work.

def salcalc_under40(hours, rate):
    s2 = float(hours) * float(rate)
    return s2

#calculation of the undertime

def undertime_snippet (hours):
    undertime= 40-float(hours)
    return float(undertime)

# Functional Code

try:
    if float(hours) > 40:
        salary1=salcalc_over40(hours, rate)
        salary_over40=str(salary1)
        print((("Hi! %s, your salary is Euro ") % name)+salary_over40)
        OVERTIME=overtime_snippet(hours)
        OVERTIME_STRING=str(OVERTIME)
        print(("You had an overtime of ")+OVERTIME_STRING+(" hours"))
        print ("Well Done. Work Less, next month! :)")


    elif float(hours) <= 40:
        salary2=salcalc_under40(hours, rate)
        salary_under40 = str(salary2)
        print(((("Hi! %s, your salary is Euro ") % name) + salary_under40))
        UNDERTIME=undertime_snippet(hours)
        UNDERTIME_STRING=str(UNDERTIME)
        print(("You worked ") + UNDERTIME_STRING + (" hours less, last month"))
        print ("We can find some work for you! ;)")

except ValueError:
    print("Please Use Numeric Input :(")