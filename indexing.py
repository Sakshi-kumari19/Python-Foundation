# indexing - accessing elements of a sequence using []
# [start : end : step]

# get last 4 digit of a credit card number

credit_number = '3241-4476-6487-6521'

last_digits = credit_number[-4:]
print(f'xxxx-xxxx-xxxx-{last_digits}')
print(credit_number[::-1]) #reverse the number

# Email Slicer 
email = input("Enter your email: ")
index = email.index('@')

username = email[:index]
domain = email[index+1:]

print(f"username: {username}")
print(f"domain: {domain}")
