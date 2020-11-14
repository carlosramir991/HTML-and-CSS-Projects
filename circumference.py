def circumv():
    radius = input("Please enter a numeric value for your radius:")
    pi = 3.141
    circumcalc(radius,pi)

def circumcalc(radius,pi):
    try:
        c = pi * 2 * int(radius)
        print("The Circumference of your circle is: {}.".format(c))
    except:
        print("You need to enter a numeric value my dude.")
        


if __name__ == "__main__":
    circumv()
    
    
    
