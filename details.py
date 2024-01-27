'''
We will request the first input from the user and ask them to store it into the variable called 'name'.
'''

# this is where we type our name
name=input("Please enter your name : ") 

'''
We will request the second input from the user and ask them to store it into the second variable called 'age'.
'''

# this is where we type our age
age=input("Please enter your age : ") 

'''
We will request the third input from the user and ask them to store it into the third variable called 'housenumber'.
'''

# this is where we type our house number
housenumber=input("Please enter your house number : ") 

'''
We will request the fourth input from the user and ask them to store it into the fourth variable called 'streetname'.
'''

# this is where we type our street name
streetname=input("Please enter your street name : ") 

'''
We print out the 'sentence' using all the inputs that you have typed for the different variables above 
The print function is used to display the sentence and the 'f' function is used to make sure that all the input we have typed are included in the sentence.
'''

# this is where the sentence with all of the user's inputs are displayed.
# if we want to type the sentence 'This is John. He is 28 years old and lives at house number 42 on Hamilton street.' We must include all the inputs that are used in this sentence for the function below.
sentence=print(f"This is {name}. He is {age} years old and lives at house number {housenumber} on {streetname} street.") 

'''
This is John. He is 28 years old and lives at house number 42 on Hamilton street.
'''