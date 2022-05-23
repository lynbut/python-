#lynse butson 
spam = ['toward','clear', 'last', 'task','family','leader','say','indicate','military','hit','available','equal','find', ['purple','needle', 7895,'clearly'], 'forty','indside', ['during', 'very', 'pilot', 'region'], 'seems', 'discover' ]
prompt = "Please select from the following choices: \n 1 Display the list \n 2 Add an item to the list at the end \n 3 Add an item to the list at the start \n 4 Add an item to the list at the end \n 5 Delete an item from the list by name \n 6 Delete the first item \n 7 Delete the last item \n 8 Delete an item by position \n 9 Show the first N items \n 10 Show the last N items \n 11 Check if an item is in the list \n 12 Add a cat named Eric the list \n 13 End \n Enter you Choice: "
print(prompt)

x = int(input())

while x != 13:
    if x == 1:
        print(spam)
        break
    elif x == 2:
        spam.append(input('What do you want to add?'))
        print(spam)
    elif x == 3:
        spam.insert(0,input('What do you want to add?'))
        print(spam)
    elif x == 4:
        spam.insert(input('What position?'),input('What word?'))
    elif x == 5:
        spam.remove(input('What item do you want to delete?'))
        print(spam)
    elif x == 6:
        del spam[0]
        print(spam)
    elif x == 7:
        del spam[-1]
        print(spam)
    elif x == 8:
        del spam[int(input('What position?'))]
        print(spam)
    elif x == 9:
        print(spam[0:int(input('enter the number of the last item you want to see'))])
    elif x == 10:
        print(spam[int(input('Enter the first position')):int(input('Enter the second position'))])
    elif x == 11:
        print(spam.index(input('Enter the item you want to search for?')))
    elif x == 12:
        spam.append('Eric the cat')
        print(spam)

    