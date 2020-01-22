userstring = input('Enter your sentence: ')

# remove all spaces
userstring = userstring.replace(" ", "")

# print forst 10 chars
print(userstring[0:10].lower())