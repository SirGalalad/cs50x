"""WHILE LOOPS"""
"""This is one way to write it"""
# i = 3
# while i != 0:
#     print("meow")
#     i = i - 1

"""This is another way"""
# get started starting numbers at 0 
# i = 0
# while i < 3:
    # print("meow")
    # i = i + 1
"""A better way to write the i + 1 is below"""
    # i += 1

"""FOR LOOPS"""
# for i in [0, 1, 2]: this is okay to use a list but range is better
# for i in range(3): 
# the best thing to do if the variable your using doesn't really need to be defined is to just use "_" to signify to yourself and others that you know that the variable didn't have or need an assignment. See below 
# for _ in range(3):
#     print("meow")

"""AN EVEN MORE PYTHONIC WAY TO WRITE THIS"""
# print("meow\n" * 3, end="")

"""GETTING NUMBER FROM USER"""
# while True:
#     n = int(input("What's n? "))
#     if n > 0:
#         break

# for _ in range (n):
#     print("meow")

def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            return n

def meow(n):
    for _ in range(n):
        print("meow")

main()