import math


# Initialize the tolerance
TOLERANCE = 0.000001

def newton(x):
    """Returns the square root of x."""
    # Perform the successive approximations
    estimate = 1.0
    while True:
        estimate = (estimate + x / estimate) / 2
        difference = abs(x - estimate ** 2)
        if difference <= TOLERANCE:
            break
    return estimate

def main():
    """Allows the user to obtain square roots."""
    while True:
        # Receive the input number from the user
        x = input("Enter a positive number or enter/return to quit: ")
        if x == "":
             break
        x = float(x)
        # Output the result
        print("The program's estimate is", newton(x))
        print("Python's estimate is     ", math.sqrt(x))

    main()


