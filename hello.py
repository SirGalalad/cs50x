"""
This is the older section
"""

# Ask user for their name
# name = input("What's your name? ").strip().title()

# Remove whitespace from str and Capitalize user's name with chained functions. They can be separate if necessary. Can put it all up top too. 
# name = name.strip().title()

# I like this way the best because it seems the most concise
# print(f"hello, {name}")

# print("hello, ", end="")
# print(name)

# print("hello,", name)

# print(name) I'm taking this out to try and get the output onto the same line to clean things up. I do that above by putting "+ name" after the "hello". I can also rewrite this function as: print("hello, ", name)

# It should be written as: print("hello,", name) specifically WITHOUT the space after hello since the placement of 2 or more arguments together automatically spaces the outputs.

# docs.python.org/3/library/functions is the official documentation

# Yet another way that we can write the function and have it give the output on one line is like this: print("hello, ", end="") followed on the next line by: print(name)  This makes it so that the default value of end="/n" which means "end each function with a new line" gets overridden 

# Double quotes "" vs single quotes '' doesn't matter in python, what matters is consistency. Unless you're trying to get quotes in the output. Then use different quotes for things. ie print('hello, "friend"') or even: print("hello, \"friend\"")

"""
THIS IS THE NEW SECTION FOR DEF OWN FUNCTIONS
"""
# def hello(to="world"):
#     print("hello,", to)

# hello()
# name = input("What's your name? ")
# hello(name)
# print(hello, name)

# def main():
#     name = input("What's your name? ")
#     hello(name)

# def hello(to="world"):
#      print("hello,", to)    

# main()

def introduction(name):
    print("Hello! My name is", name)

introduction("Katerina")