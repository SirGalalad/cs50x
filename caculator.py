x = float(input("What's x? "))
y = float(input("What's y? "))

# z = x + y #this doesn't work because "+" concatenates 
# z = int(x) + int(y)

# z = round(x + y, 3)
# print(f"{z:,}")


# practicing using different mathematic operations
z = round(x / y, 2)

print(z)

# another way to right the above function is z = x / y followed by print(f"{z:2f}") if you want to use fstrings

# float vs int makes the output 3.0 vs just 3, but it still treats all of the inputs as actual integers