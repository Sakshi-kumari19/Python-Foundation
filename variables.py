print('hello') #single quote
print("hello") #double quote

# Variables - conatiner for a val , it behaves as if it was the value it contains
email = "sakshi.kumari19@gmail.com" #string 
print(f"your email {email}") #formatted string

# float
cgpa = 8.8
print(f'my cgpa is {cgpa}')

# boolean
is_student = True  #used mostly internally in if/else
if is_student:
    print('yes') 
else:
    print('no') #if false

# Typecasting - process of converting one variable from one datatype to another.
# specially useful to handle user input because it is always a string & we need to convert into int, float etc
#  str(), int(), float(), bool()

name = 'sakshi'
age = 21
cgpa = 9.2
is_student = True

print(float(age))
print(str(age))

print(bool(name)) #ans = true in every case except empty string
# if name is empty it gives FALSE , use this to check if a user has given their name or not.