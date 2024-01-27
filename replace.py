# the initial sentence
sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog." 

# the sentence with '!' replaced with ' '
x = sentence.replace("!"," ") 

# the lower case letters of the sentence converted to upper case letters using upper()
y = sentence.replace("!"," ").upper() 

# the sentence above in reversed order using upper() and slicing of [::-1]
z = sentence.replace("!"," ").upper()[::-1] 

# the outcome of the sentence with exclamation mark replaced with ' '
print(x) 

# the outcome of the first sentence with the lower case letters being converted to capital letters
print(y) 

# the outcome of the second sentence being reversed in order
print(z)