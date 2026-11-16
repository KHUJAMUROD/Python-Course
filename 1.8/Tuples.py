# mytuple = tuple(("apple", "banana", "cherry"))
# print(mytuple)


# mytuple = ("apple", "banana", "cherry")
# print(mytuple)


# mytuple = "apple", "banana", "cherry"
# print(mytuple)


# thistuple = ("apple", "banana", "cherry", "apple", "cherry")
# print(thistuple) # ('apple', 'banana', 'cherry', 'apple', 'cherry')
# print(thistuple[0]) # apple
# print(thistuple[2]) # cherry


# thistuple = ("apple", "banana", "cherry")
# print(len(thistuple)) # 3


# thistuple = ("apple",)
# print(type(thistuple)) # <class 'tuple'>

# #NOT a tuple
# thistuple = ("apple")
# print(type(thistuple)) # <class 'str'>


# thistuple = ()
# print(type(thistuple)) # <class 'tuple'>


# tuple1 = ("apple", "banana", "cherry")
# tuple2 = (1, 5, 7, 9, 3)
# tuple3 = (True, False, False)
# tuple4 = ("abc", 34, True, 40, "male")


# mytuple = ("apple", "banana", "cherry")
# print(type(mytuple))  # <class 'tuple'>


# thistuple = ("apple", "banana", "cherry")
# print(thistuple[1]) # "banana"


# thistuple = ("apple", "banana", "cherry")
# print(thistuple[-1]) # "cherry"


# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[2:5]) # ("cherry", "orange", "kiwi",)


# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[:4]) # ("apple", "banana", "cherry", "orange")


# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[2:]) # ("cherry", "orange", "kiwi", "melon", "mango")


# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[-4:-1]) # ("orange", "kiwi", "melon",)


# thistuple = ("plum", "banana", "cherry")
# thistuple = ("apple", "banana", "cherry")
# if "apple" in thistuple:
#   print("Yes, 'apple' is in the fruits tuple")
# else:
#   print("Not, 'apple' is not in the fruits tuple")


# x = ("apple", "banana", "cherry")
# y = list(x)
# y[1] = "kiwi"
# x = tuple(y)

# x[1] = 'kiwi' # TypeError: 'tuple' object does not support item assignment

# print(x)


# thistuple = ("apple", "banana", "cherry")
# y = list(thistuple)
# y.append("orange")
# thistuple = tuple(y)

# print(thistuple) # ('apple', 'banana', 'cherry', 'orange')


# thistuple = ("apple", "banana", "cherry")
# y = ("orange",)
# thistuple += y

# print(thistuple) # ('apple', 'banana', 'cherry', 'orange')


# thistuple = ("apple", "banana", "cherry")
# y = list(thistuple)
# y.remove("apple")
# thistuple = tuple(y)


# print(thistuple) # ('banana', 'cherry')


# thistuple = ("apple", "banana", "cherry")
# del thistuple
# print(thistuple) #this will raise an error because the tuple no longer exists


# fruits = ("apple", "banana", "cherry")

# (green, yellow, red) = fruits

# green = fruits[0]
# yellow = fruits[1]
# red = fruits[2]

# print(green)
# print(yellow)
# print(red)


# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

# (green, yellow, *red) = fruits

# print(green) # 'apple'
# print(yellow) # 'banana'
# print(red) # ['cherry', 'strawberry', 'raspberry']


# fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

# (green, *tropic, red) = fruits

# print(green) # 'apple'
# print(tropic) # ['mango', 'papaya', 'pineapple']
# print(red) # 'cherry'


# thistuple = ("apple", "banana", "cherry")
# for x in thistuple:
#   print(x)

# # apple
# # banana
# # cherry


# print(2 < 3) # True
# print(3 < 3) # False
# thistuple = ("apple", "banana", "cherry")
# for i in range(3):
    # print(thistuple[i], i)

#  apple
#  banana
#  cherry




# thistuple = ("apple", "banana", "cherry")
# i = 0
# while i < len(thistuple):
#   print(thistuple[i])
#   i += 1
#   i = i + 1



#  apple
#  banana
#  cherry




# tuple1 = ("a", "b" , "c")
# tuple2 = (1, 2, 3)

# tuple3 = tuple1 + tuple2
# print(tuple3) # ('a', 'b', 'c', 1, 2, 3)


# fruits = ("apple", "banana", "cherry")
# mytuple = fruits * 2

# print(mytuple) # ("apple", "banana", "cherry", "apple", "banana", "cherry")




# thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5, 7, 7)
# x = thistuple.count(7)
# print(x) # 4



# thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
# x = thistuple.index(8)
# print(x) # 3
# x = thistuple.index(8, 4)
# print(x) # 8
# x = thistuple.index(8, 2, 5)
# print(x) # 3
# x = thistuple.index(8, -5)
# print(x) # 8
# x = thistuple.index(8, -5, -7)
# print(x) # error


