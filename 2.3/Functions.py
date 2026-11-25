# def my_function():
#   print("Hello from a function")

# my_function()
# my_function()
# my_function()




# temp1 = 77
# celsius1 = (temp1 - 32) * 5 / 9
# print(celsius1) # 25.0

# temp2 = 95
# celsius2 = (temp2 - 32) * 5 / 9
# print(celsius2) # 35.0

# temp3 = 50
# celsius3 = (temp3 - 32) * 5 / 9
# print(celsius3) # 10.0


# def fahrenheit_to_celsius(fahrenheit):
#   return (fahrenheit - 32) * 5 / 9

# print(fahrenheit_to_celsius(77)) # 25.0
# print(fahrenheit_to_celsius(95)) # 35.0
# print(fahrenheit_to_celsius(50)) # 10.0




# def get_greeting():
#   return "Hello from a function"

# message = get_greeting()
# print(message) # Hello from a function



# def get_greeting():
#   return "Hello from a function"

# print(get_greeting()) # # Hello from a function



# def test_Fn():
#     print("Test Fn") # Test Fn

# some_Info_from_Fn = test_Fn()

# print(some_Info_from_Fn)  # None



# def my_function():
#   pass




# def my_function(fname):
#   print(fname + " Refsnes")

# my_function("Emil") # Emil Refsnes
# my_function("Tobias") # Tobias Refsnes
# my_function("Linus") # Linus Refsnes




# def my_function(fname, lname):
#   print(fname + " " + lname)

# my_function("Emil", "Rafael") # Emil Rafael



# def my_function(fname, lname):
#   print(fname + " " + lname)

# my_function("Emil") # Error



# def my_function(name = "friend"):
#   print("Hello", name)

# my_function("Emil") # Hello Emil
# my_function("Tobias") # Hello Tobias
# my_function() # Hello friend
# my_function("Linus") # Hello Linus



# def my_function(country = "Norway"):
#   print("I am from", country)

# my_function("Sweden") # I am from Sweden
# my_function("India") # I am from India
# my_function() # I am from Norway
# my_function("Brazil") # I am from Brazil



# def my_function(animal, name):
#   print("I have a", animal)  # I have a dog
#   print("My", animal + "'s name is", name)  # My dog's name is Buddy

# my_function(animal = "dog", name = "Buddy") 



# def my_function(animal, name):
#   print("I have a", animal) # I have a dog
#   print("My", animal + "'s name is", name) # My dog's name is Buddy

# my_function(name = "Buddy", animal = "dog")




# def my_function(name, animal):
# def my_function(animal, name):
#   print("I have a", animal)
#   print("My", animal + "'s name is", name)

# my_function("dog", "Buddy")


# def my_function(animal, name):
#   print("I have a", animal) # I have a Buddy
#   print("My", animal + "'s name is", name) # My Buddy's name is dog

# my_function("Buddy", "dog")



# def my_function(animal, name, age):
#   print("I have a", age, "year old", animal, "named", name)# I have a 5 year old dog named Buddy
  

# my_function("dog", name = "Buddy", age = 5)




# def my_function(fruits):
#   for fruit in fruits:
#     print(fruit)

# my_fruits = ["apple", "banana", "cherry"]
# my_function(my_fruits)

# apple
# banana
# cherry



# def my_function(person):
#   print("Name:", person["name"]) # Name: Emil
#   print("Age:", person["age"]) # Age: 25

# my_person = {"name": "Emil", "age": 25}
# my_function(my_person)




# def my_function(x, y):
#   return x + y

# result = my_function(5, 3)
# print(result) # 8



# def my_function():
#   return ["apple", "banana", "cherry"]


# fruits = my_function()
# print(fruits[0]) # apple
# print(fruits[1]) # banana
# print(fruits[2]) # cherry



# def my_function():
#   return (10, 20)

# x, y = my_function()
# print("x:", x) # x: 10
# print("y:", y) # y: 20




# def my_function(name, /):
#   print("Hello", name)

# my_function("Emil",) # Hello Emil



# def my_function(name):
#   print("Hello", name) # # Hello Emil

# my_function(name = "Emil")


# def my_function(name, /):
#   print("Hello", name)

# my_function(name = "Emil") # Error



# def my_function(name):
#   print("Hello", name) # Hello Emil

# my_function("Emil")




# def my_function(*, name):
#   print("Hello", name)

# my_function("Emil")  # Error


# a = 5
# b = 10
# def my_function(a, b, /, *, c, d):
#   return a + b + c + d

# result = my_function(5, 10, c = 15, d = 20) # 50
# result = my_function(a, b, c = 15, d = 20) # 50
# result = my_function(a, b, 15, 20) # Error
# print(result)



