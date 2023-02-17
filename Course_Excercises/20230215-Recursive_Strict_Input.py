def input_as_int():
    try:
        user_age = int(input('how old are you? '))
        user_brothers = int(input('how many brothers do you have? '))
        print()
        #if all(x>=0 for x in [user_age,user_brothers]):
        if 0 < user_age < 150:
            print(f"Your age is: {user_age}, and you have {user_brothers} brothers")
            if user_brothers == 0:
                print('you are a single person\n')
            elif 1 < user_brothers < 6:
                print("You are lucky person")
            else:
                print('WOW, you have a LOT of problems')
        else: raise ValueError
    except ValueError:
        print('Please, enter an integer')
        input_as_int()
print('\n--------------INPUT WITH INTEGER CONDITION-----------------\n')
input_as_int()
