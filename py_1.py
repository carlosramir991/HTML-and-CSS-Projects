import os

fPath = '/Users/slims/Documents/python_assig'

files = os.listdir(fPath)

length = len(files)

for i in range(length):
    if files[i].endswith('.txt'):
        print(files[i])

        


    




        
        
    




