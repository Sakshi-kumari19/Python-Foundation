# format the value based on the flags inserted
# {value:specifier}

price1 = 3.2321
price2 = -897.97
price3 = 22.23

print(f"price1: {price1:.2f}")
print(f"price2: {price2:.2f}")
print(f"price3: {price3:.2f}")
# price1: 3.23
# price2: -897.97
# price3: 22.23

# i need to present the data in 10 digits
print(f"price1: {price1:10}")
print(f"price2: {price2:10}")
print(f"price3: {price3:10}")
# price1:     3.2321
# price2:    -897.97
# price3:      22.23

# zero padded
print(f"price1: {price1:010}")
print(f"price2: {price2:010}")
print(f"price3: {price3:010}")
# price1: 00003.2321
# price2: -000897.97
# price3: 0000022.23

# left justified
print(f"price1: {price1:<10}")
print(f"price2: {price2:<10}")
print(f"price3: {price3:<10}")

# right justified
print(f"price1: {price1:>10}")
print(f"price2: {price2:>10}")
print(f"price3: {price3:>10}")

# center justified
print(f"price1: {price1:^10}")
print(f"price2: {price2:^10}")
print(f"price3: {price3:^10}")

# positive val and shhow its sign
print(f"price1: {price1:+}")
print(f"price2: {price2:+}") #show -ve as num is neg
print(f"price3: {price3: }")# space works same as +

# place , after 1000 place
a = 2999.43443
print(f"{a:,}")
# using 3 specifier + , .2f
print(f'{a:+,.2f}')

