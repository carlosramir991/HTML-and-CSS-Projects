import sys

def factorial(x, offset=''): 
    #base case (EVERY RECURSIVE MUST HAVE A BASE CASE AND THE RESULT MUST APPROACH THE BASE CASE!!)
    if x <= 1:
        print(offset, 1)
        return 1
    # recursive case
    print(offset, x)
    result = x * factorial(x-1, offset + "   ")
    print(offset, result)
    return result

def main():
    print(factorial(6))
#MUST ENTER THE DUNDER TRICK
main()
