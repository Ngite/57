


str="hellow"
print(str);

#accessing the character in string
str="hellow"
print(str[0])
print(str[2])


#TO DELETE CHARACTER
str="hello"
print(str)
str=str[0:2]+str[3:]
print(str)

#TO DELETE STRING
str="hellow"
print(str)
del str
print(str)

#string character updation
original_string = "hellow"

"""
replaced character is w, and it is present at the 2nd index so storing its index for future replacement
"""
index = 5

# ``p`` will replace ``w`
new_character = "p"

original_string = original_string[:index] + new_character + original_string[index + 1:]

print(original_string)



#escpae sequence
str="hellow\'how are you\'"
print(str)

#ALIGNMENT TEXT
str='{:<20}{:^20}{:>20)'
format('hellow','hi','welcome')
print(str)
