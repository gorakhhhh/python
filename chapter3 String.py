                                 #  String
# String is a sequence of characters enclosed in quotes.
# We can primarily write a string in these three ways.

# a = "gorakh" # double quotes string
# b = ' gorakh1' #single quotes string
# c = ''' gorakh ''' # triple quotes 
 
# print(type(a))


                               #  Traversal with a loop: is a process of accessing each character of string

# a ="gorakh"
# b = 0

# for b in a:
#     print(b,end="")

                                       #slicing string

# a = "gorakhnath"
# print(a[1])
# print(a[2]) # range start from 0 and can me negative also
# print(a[3])                    
# print(a[-4])
# print(a[-5])
# print(a[0:4])# it is range that start from 0 and end with 3 so ans is gora.
# print(a[1:2:2])# staring,ending and hope.it will always take hope-1 to hope if there is 2 it will take hope of 1


                                             # count 
# word = "banana"
# count = 0
# for letter in word:
#     if letter == 'a':
#         count = count + 1
# print(count)        


                                               # String operation
# 1.concatenation
# a ="ram"
# b =" hari"

# for i in a:
#     print(i+b)

# c = "apple"
# d = "banana"

# e=c+d
# print(e)

#2.repetition

# a = "gorakh"
# print(a[2]*3)


# 3.membership
#p in a
#s not in a
                                           # string function
# Sample string
sample_text = "  Hello, Python World!  "


# # 1. strip() - Removes leading and trailing whitespaces
# print("strip():", sample_text.strip())

# # 2. lower() - Converts all characters to lowercase
# print("lower():", sample_text.lower())

# # 3. upper() - Converts all characters to uppercase
# print("upper():", sample_text.upper())

# # 4. capitalize() - Capitalizes the first character
# print("capitalize():", sample_text.strip().capitalize())

# # 5. title() - Converts the first character of each word to uppercase
# print("title():", sample_text.strip().title())

# # 6. replace() - Replaces occurrences of a substring with another substring
# print("replace('Python', 'Coding'):", sample_text.replace("Python", "Coding"))

# # 7. split() - Splits the string into a list
# print("split():", sample_text.strip().split())

# # 8. join() - Joins elements of a list into a string
# words = sample_text.strip().split()
# print("join():", "-".join(words))

# # 9. find() - Returns the index of the first occurrence of a substring
# print("find('Python'):", sample_text.find("Python"))

# # 10. isalpha() - Checks if all characters are alphabetic (ignoring spaces)
# print("isalpha():", "Python".isalpha())

# # 11. count() - Counts occurrences of a substring
# print("count('o'):", sample_text.count("o"))

# # 12. startswith() - Checks if the string starts with a specific substring
# print("startswith('  Hello'):", sample_text.startswith("  Hello"))

# # 13. endswith() - Checks if the string ends with a specific substring
# print("endswith('World!  '):", sample_text.endswith("World!  "))

# # 14. len() - Gets the length of the string
# print("len():", len(sample_text))



letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''
print(letter.replace("<|Name|>","gorakh").replace("<|Date|>","12 june 2003"))
