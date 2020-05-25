def start():
    people_dictionary={'Brett':['Male','Weight 175'],
    'nancy':['Female','Weight 125'],'patrick':['Male','Weight'],
    'diane':['Female','Weight 115'], 'adam':['Male','Weight 215']}
    print(people_dictionary)
    Name=input('Please type in a name: ').lower()
    print('You typed in the name '+ Name.capitalize())
    try:
        Persons_Data=people_dictionary[Name]
        print('Name: '+Name.capitalize())
        print('Sex: '+Persons_Data[0])
        print('Weight: '+Persons_Data[1])
        more()
    except:
        print('That name (as written) was not fount in the dictionary.')
        more()
def more():
    more=input('Would you like to search for another name?: ')
    if more=='No':
        quit()
    if more=='Yes':
        start()
    else:
        print('Please enter Yes or No.')
        more()
start()

    




