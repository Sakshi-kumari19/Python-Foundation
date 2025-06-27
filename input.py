# User input - function that prompts user to enter data & returns that data as a string.
name = input("what is your name?: ") # the string inside is prompt
age = int(input('what is your age?: '))

age = age + 1
print(f'Hello {name}')
print("Happy Birthday!!")
print(f"Your age is {age}")

# Q. rectangle area 
length = float(input("Enter length: "))
width = float(input("Enter width: "))
area = length * width # if both are strings ,gives error
print(f"The area is: {area}cm2")

# Q.shopping cart 
item = input("What item would you buy?: ")
price  = float(input("What is the price?: "))
quantity = int(input("How many would you like?: "))
total = price * quantity

print(f"You have bought {quantity} x {item}/s")
print(f"Total: Rs {total}")
