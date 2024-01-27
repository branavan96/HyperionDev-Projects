# this is where we type the sentence
str_manip = input("Please enter a sentence : ")

# the output of the sentence
print(str_manip)

# the output of the length of the sentence
print(len(str_manip))

# if the last letter of a sentence is 's', any word in the sentence with 's' in it would be replaced with '@'
str_manip_rep= str_manip.replace("s","@")

# the output of the sentence with words that have some letter replaced with '@'
print(str_manip_rep)

# the output of the last three letters of a sentence printed backwards
print(str_manip[-3:][::-1])

# the word is formed by using two different types of slicing and adding them together
new_word = str_manip[0:3] + str_manip[-2][::1]

# the output of the new five-letter word
print(new_word)