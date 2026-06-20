rawstr = input("Enter a number: ")

try:
    intvalue = int(rawstr) # If user entred the string instead of number try will fail,
                            #and catch take control of the code
except:
    intvalue = -1


if intvalue > 0 :
    print("Nice work! you have entered the number.")
elif intvalue == -1:
    print("Not a number ")