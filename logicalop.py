# logical operator = used on conditional statements
# and, or, not

# and - checks 2 or more condition
# or - checks at least 1 is true
# not - trye if condition is false

# Conditional expression - shortcut for if -else
#                          ternary operator -> (X if condition else Y)
# eg1
num = 5

print("Positive" if num>0 else "Negative")
print("Even" if num % 2 == 0 else "Odd")

# eg2
age = 25
print("Adult" if age>=18 else "Child")

# eg3
user_role = 'guest' #write admin
access_level = "Full Access" if user_role == 'admin' else "Access Denied"

print(access_level)