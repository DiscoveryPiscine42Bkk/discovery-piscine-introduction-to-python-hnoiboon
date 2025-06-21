print('Enter a number:')
number_entered = input()
if int(number_entered) == 0 :
    print("This number is both positive and negative")
if int(number_entered) > 0 :
    print("This number is positive")
if int(number_entered) < 0 :
    print("This number is negative")