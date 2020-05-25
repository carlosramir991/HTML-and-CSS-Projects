
def factorial(x): 
    #base case (EVERY RECURSIVE MUST HAVE A BASE CASE AND THE RESULT MUST APPROACH THE BASE CASE!!)
    if x <= 1:
        return 1
    # recursive case
    return x * factorial(x-1)

def main():
    print(factorial(6))
#MUST ENTER THE DUNDER TRICK
main()