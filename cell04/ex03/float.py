user_input = input("Give me a number:")
user_input_float = float(user_input)
if user_input_float.is_integer():
    print("This number is an integer")
else:
    print("This number is a decimal")    
