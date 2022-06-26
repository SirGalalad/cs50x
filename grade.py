score = int(input("Score: "))

'''First way to write this'''
# if score >= 90 and score <= 100:
#     print("Grade: A")

# elif score >= 80 and score < 89:
#     print("Grade: B")

# elif score >=70 and score < 80:
#     print("Grade: C")

# elif score >=60 and score < 70:
#     print("Grade: D")

# else:
#     print("Grade: F")

'''Second way to write this'''
# By having the first statement ask if followed by elif, it makes it so that the other statements are inheriting the learned value to then assign the correct score
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")