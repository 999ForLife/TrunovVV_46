dic = {'one': 1, 'two': 2, 'three': 3}

while True:
    your_input = input('Type in word ("one", "two" or "three"): ')
    if your_input == 'Bye' or your_input == 'bye':
        print('It was fun! Goodbye...')
        break
    elif dic.get(your_input) != None:
        print(f'Good job! Value for this key is: {dic.get(your_input)}')
    else: print('There is no such key :( Try again!\n')

print("\nПривет из прошлого проверяющим курса!")
