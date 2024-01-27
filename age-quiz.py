# Using if/elif for conditional statements, the user is prompted to input their age (the variable 'age').
# After that step, we use the print function to display the age and related message for that age, dependent on the age range it falls within.
# The code become more complicated when we type words into the variable 'age' which gives error messages.
try:
    age = int(input("Please enter your age : "))
    print(age)
    
    if age >= 40 and age < 65:
        print("You're over the hill.")
    elif age >= 100:
        print("Sorry, you're dead.")
    elif age >= 65 and age < 100:
        print("Enjoy your retirement!")
    elif age < 13: 
        print("You qualify for the kiddie discount.")
    elif age == 21: 
        print("Congrats on your 21st!")
    else: 
        print("Age is but a number.")
except ValueError:
    print("That's not a valid age. Please enter a number.")