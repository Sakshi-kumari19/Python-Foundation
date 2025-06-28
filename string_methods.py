# 1.
"""name = input("Enter your full name: ")
phone = '3423-5434-343'
print(len(name)) #return int
print(name.find(" ")) # return first occurrence of given char
print(name.rfind(" ")) #return last occurrence
# if cant locate it will return -1

print(name.capitalize()) #return string first letter is capitalize
print(name.upper())
print(name.lower())
print(name.isdigit())# return t/f , it return True if string contains only number
# fkdf434-> False
print(name.isalpha()) # sakshi kumari-> False , because of space
# gjfk434 -> false

print(phone.count("-"))
print(phone.replace("-", " "))

print(help(str)) #to find all the inbuilt functions"""

""" Enter your full name: sakshi kumari
13
6
6
Sakshi kumari
SAKSHI KUMARI
sakshi kumari
False
False
2
3423 5434 343
Help on class str in module builtins:

class str(object)
 |  str(object='') -> str
 |  str(bytes_or_buffer[, encoding[, errors]]) -> str
 |
 |  Create a new string object from the given object. If encoding or
 |  errors is specified, then the object must expose a data buffer
 |  that will be decoded using the given encoding and error handler.
 |  Otherwise, returns the result of object.__str__() (if defined)
-- More  --"""

# validate user input
# 1. username <= 12 char
# 2.not contain spaces
# 3.not contain digits

username = input("Enter your name: ")

# if len(username) > 12:
#     pass
# elif username.find(" ") > 0:
#     pass
# elif username.isalpha():
#     pass
# else:
#     pass

if len(username) > 12 or username.find(" ") or not username.isalpha():
    print("Invalid username!!")
else: 
    print("Valid Username!!")

