# print("He'l\"lo")
# print('He\'l"lo')
# print("It's alright")


# a = "He\nllo"
# print(a)

# a = """Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua."""
# print(a)


# a = '''Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua.'''
# print(a)



# a = "Hello, World!"
# print(a[1]) # 'e'
# print(a[1:5]) # 'ello'
# print(a[1:]) # 'ello, World!'



# for x in "banana":
#   print(x)  
# b
# a
# n
# a
# n
# a


# a = "Hello, World!"
# print(len(a)) # 13
# print(a[len(a) - 1]) # !


# txt = "The best things in life are free!"
# print("free" in txt) # True
# print("freeabc" in txt) # False


# txt = "The best things in life are free!"
# if "free" in txt: # True
#   print("Yes, 'free' is present.")


# txt = "The best things in life are free! "
# print("expensive" not in txt) # True



# txt = "The best things in life are free!"
# if "expensive" not in txt: # True
#   print("No, 'expensive' is NOT present.")


# b = "Hello, World!"
# print(b[2:5]) # llo


# b = "Hello, World!"
# print(b[:5]) # Hello

# b = "Hello, World!"
# print(b[2:]) # llo, World!



# b = "Hello, World!"
# print(b[-5:-2]) # orl
# print(b[-10:-5]) # lo, W
# print(b[-5:-7]) # ''


# a = "Hello, World!"
# print(a.upper()) # HELLO, WORLD!

# a = "Hello, World!"
# print(a.lower()) # hello, world!


# a = "     Hello, World!     "
# print(a) # returns "     Hello, World!     "
# print(a.strip()) # returns "Hello, World!"


# a = "Hello, World!"
# print(a.replace("H", "J")) # 'Jello, World!'



# a = "Hello, World!"
# print(a.split(",")) # returns ['Hello', ' World!']
# print(a.split(" ")) # returns ['Hello,', 'World!']


# a = "Hello"
# b = "World"
# c = a + b
# print(c) # HelloWorld


# a = "Hello"
# b = "World"
# c = a + " " + b
# print(c)



# age = 36
# #This will produce an error:
# txt = "My name is John, I am " + age # Error
# print(txt) 


# age = 36
# txt = f"My name is John, I am {age}"
# print(txt) # My name is John, I am 36


# price = 59
# txt = f"The price is {price} dollars"
# print(txt) # The price is 59 dollars


# price = 59
# txt = f"The price is {price:.2f} dollars"
# print(txt) # The price is 59.00 dollars


# txt = f"The price is {20 * 59} dollars"
# print(txt) # The price is 1180 dollars


# Negatives in Pyhthon => False, '', 0, None, (), {}, [], 0j, range(0)
# print(bool(-123)) # True
# print(bool(0)) # False


# txt = "We are the so-called "Vikings" from the north." # error
# txt = "We are the so-called \"Vikings\" from the north." # correct


