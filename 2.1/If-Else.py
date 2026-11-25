# a = 33
# b = 200
# if b > a:
#     print("b is greater than a") # b is greater than a


# number = 15
# if number > 0:
#   print("The number is positive") # "The number is positive"


# a = 33
# b = 200
# if b > a:
# print("b is greater than a")  # you will get an error because of space before print


# age = 20
# if age >= 18:
#     print("You are an adult") # You are an adult
#     print("You can vote") # You can vote
#     print("You have full legal rights") # You have full legal rights


# is_logged_in = True
# if is_logged_in:
#   print("Welcome back!") # "Welcome back!"


# a = 33
# b = 33
# if b > a:
#     print("b is greater than a")
# elif a == b:
#     print("a and b are equal") # "a and b are equal"


# score = 60

# if score >= 90:
#   print("Grade: A")
# elif score >= 80:
#   print("Grade: B")
# elif score >= 70:
#   print("Grade: C")
# elif score >= 60:
#   print("Grade: D") # "Grade: D"


# age = 25

# if age < 13:
#   print("You are a child")
# elif age < 20:
#   print("You are a teenager1")
# elif age < 30:
#   print("You are a teenager2") # "You are a teenager2"
# elif age < 65:
#   print("You are an adult")
# elif age >= 65:
#   print("You are a senior")


# day = 3

# if day == 1:
#   print("Monday")
# elif day == 2:
#   print("Tuesday")
# elif day == 3:
#   print("Wednesday") # "Wednesday"
# elif day == 4:
#   print("Thursday")
# elif day == 5:
#   print("Friday")
# elif day == 6:
#   print("Saturday")
# elif day == 7:
#   print("Sunday")


# a = 200
# b = 33
# if b > a:
#   print("b is greater than a")
# elif a == b:
#   print("a and b are equal")
# else:
#   print("a is greater than b") # a is greater than b


# a = 200
# b = 33
# if b > a:
#   print("b is greater than a")
# else:
#   print("b is not greater than a") # b is not greater than a


# number = 7

# if number % 2 == 0:
#   print("The number is even")
# else:
#   print("The number is odd") # The number is odd"


# temperature = 5

# if temperature > 30:
#   print("It's hot outside!")
# elif temperature > 20:
#   print("It's warm outside")
# elif temperature > 10:
#   print("It's cool outside")
# else:
#   print("It's cold outside!") # It's cold outside!


# username = "Maftuna"

# if len(username) > 0:
#   print(f"Welcome, {username}!")  # Welcome, Maftuna!
# else:
#   print("Error: Username cannot be empty")


# a = 5
# b = 2
# if a > b: print("a is greater than b") # a is greater than b


# a = 2
# b = 330
# print("A") if a > b else print("B") # "B"


# a = 10
# b = 20
# bigger = a if a > b else b
# print("Bigger is", bigger) # Bigger is 20


# a = 330
# b = 330
# print("A") if a > b else print("=") if a == b else print("B") # =


# x = 15
# y = 20
# max_value = x if x > y else y
# print("Maximum value:", max_value)


# username = ""
# display_name = username if username else "Guest"
# print("Welcome,", display_name) # Welcome, Guest


# a = 200
# b = 33
# c = 500
# if a > b and c > a:
#   print("Both conditions are True") # Both conditions are True
#   print(a > b and c > a) # True


# a = 200
# b = 33
# c = 500
# if a > b or a > c:
#   print("At least one of the conditions is True") # At least one of the conditions is True
#   print(a > b or a > c) # True


# a = 33
# b = 200
# if not a > b:
#   print("a is NOT greater than b") # a is NOT greater than b
#   print(not a > b) # True
#   print( a > b) # False


# age = 25
# is_student = False
# has_discount_code = True

# if (age < 18 or age > 65) and not is_student or has_discount_code:
#   print("Discount applies!")


# username = "Tobias"
# password = "secret123"
# is_verified = True

# if username and password and is_verified:
#   print("Login successful")
# else:
#   print("Login failed")


# score = 85

# if score >= 0 and score <= 100:
#   print("Valid score")
# else:
#   print("Invalid score") # "Invalid score"


# x = 41

# if x > 10:
#   print("Above ten,")  # "Above ten,"
#   if x > 20:
#     print("and also above 20!") # "and also above 20!"
#   else:
#     print("but not above 20.")


# score = 70
# attendance = 90
# submitted = True

# if score >= 60:
#   if attendance >= 80:
#     if submitted:
#       print("Pass with good standing") # "Pass with good standing"
#     else:
#       print("Pass but missing assignment")
#   else:
#     print("Pass but low attendance")
# else:
#   print("Fail")


# temperature = 25
# is_sunny = True

# if temperature > 20:
#     if is_sunny:
#         print("Perfect beach weather!") # "Perfect beach weather!"


# if temperature > 20 and is_sunny:
#     print("Perfect beach weather!") # "Perfect beach weather!"


# username = "Emil"
# password = "python123"
# is_active = True

# if username:
#     if password:
#         if is_active:
#             print("Login successful") # "Login successful"
#         else:
#             print("Account is not active")
#     else:
#         print("Password required")
# else:
#     print("Username required")

# if username and password and is_active:
#     print("Login successful") # "Login successful"


# score = 85
# extra_credit = 3

# if score >= 90 or 86 <= score:
#   if extra_credit > 2:
#     print("A+ grade")
#   else:
#     print("A grade")
# elif score >= 85 or score >= 80:
#   print("B grade")
# else:
#   print("C grade or below")


# a = 33
# b = 200

# if b > a:
#   pass # continue


# age = 20

# if age < 18:
#   pass # TODO: Add underage logic later
# else:
#   print("Access granted") # continue


# score = 85

# if score > 90:
# This is excellent
# This will raise an IndentationError

# score = 85

# if score > 90:
    # pass  # This is excellent
# print("Score processed")



# value = 50

# if value < 0:
#   print("Negative value")
# elif value == 0:
#   pass # Zero case - no action needed
# else:
#   print("Positive value") # Positive value



# def calculate_discount(price):
#   pass # TODO: Implement discount logic

# Function exists but doesn't do anything yet





