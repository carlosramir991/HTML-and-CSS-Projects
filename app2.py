import app

def printApp2():
    name = (__name__)
    return name

if __name__ == "__main__":
    print("You are now using {}.".format(printApp2()))


    print("You are also using {}.".format(app.printApp()))
