try: 
    hours = int(input("Enter hours: "))
    rate = float(input("Enter rate: "))
    pay = 0
    extra = 0
except:
    print("Error, please enter numeric input")
    quit()
if hours <= 40:
        pay = hours * rate
        print("Pay: $", pay)
elif hours > 40:
    extraHours = hours - 40 
    extra = extraHours * 1.5
    pay = 40 * rate + extra * rate
    print("It seems like you did extra hours. your pay is: $", pay, ". And you worked ", extraHours, " extra hours")
     
