# x = int(input("What's x? "))

# if x % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    # make more sense to me to be written like: "return True if n % 2 == 0 else False" but the code underneath is the most concise way to do it
    return n % 2 == 0   

main()