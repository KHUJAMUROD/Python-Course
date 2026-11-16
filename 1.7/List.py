# thislist = ["apple", "banana", "cherry"]
# mytuple = ("apple", "banana", "cherry")
# myset = {"apple", "banana", "cherry"}

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964,
# }

# print(thislist)
# print(mytuple)
# print(myset)
# print(thisdict)


# thislist = ["apple", "banana", "cherry"]
# print(len(thislist)) # 3


# thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
# thisset = set(("apple", "banana", "cherry"))   # note the double round-brackets
# thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets

# thisdict = dict(
#     brand = "Ford",
#     model = "Mustang",
#     year = 1964,
# )

# print(thislist)
# print(thisset)
# print(thistuple)
# print(thisdict)


# list1 = ["apple", "banana", "cherry"]
# list2 = [1, 5, 7, 9, 3]
# list3 = [True, False, False]
# list4 = ["abc", 34, True, 40, "male"]

# mylist = ["apple", "banana", "cherry"]
# print(type(mylist)) # <class 'list'>


# thislist = ["apple", "banana", "cherry"]
# print(thislist[-1]) # 'cherry'


# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:5]) # ['cherry', 'orange', 'kiwi']


# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[:4]) # ['apple', 'banana', 'cherry', 'orange']


# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:])  # ['cherry', 'orange', 'kiwi', 'melon', 'mango']


# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[-4:]) # ['orange', 'kiwi', 'melon', "mango"]
# print(thislist[-4:-5]) # []


# thislist = ["apple", "banana", "cherry"]
# print("apple" in thislist)  # True


# if "apple" in thislist:
#   print("Yes, 'apple' is in the fruits list")


# thislist = ["apple", "banana", "cherry"]
# thislist[1] = "blackcurrant"
# print(thislist) #  ['apple', 'blackcurrant', 'cherry']


# thislist = ["apple", "banana", "cherry"]
# thislist[1:2] = ["blackcurrant", "watermelon"]
# print(thislist) # ['apple', 'blackcurrant', 'watermelon', 'cherry']


# thislist = ["apple", "banana", "cherry"]
# thislist[1:3] = ["watermelon"]
# print(thislist) # ['apple', 'watermelon']


# thislist = ["apple", "banana", "cherry"]
# thislist.insert(2, "watermelon")
# print(thislist)  # ['apple', 'banana', 'watermelon', 'cherry']


# thislist = ["apple", "banana", "cherry"]
# thislist.append("orange")
# print(thislist) # ['apple', 'banana', 'cherry', 'orange']


# thislist = ["apple", "banana", "cherry"]
# thislist.insert(1, "orange")
# print(thislist) # ['apple', 'orange', 'banana', 'cherry']


# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]
# thislist.extend(tropical)
# print(thislist) # ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']


# thislist = ["apple", "banana", "cherry"]
# thistuple = ("kiwi", "orange")
# thislist.extend(thistuple)
# print(thislist) # ['apple', 'banana', 'cherry', 'kiwi', 'orange']
# thistuple.extend(thislist)
# print(thistuple) # AttributeError: 'tuple' object has no attribute 'extend'


# thislist = ["apple", "banana", "cherry"]
# thislist.remove("banana")
# print(thislist)  # ['apple', 'cherry']


# thislist = ["apple", "banana", "cherry"]
# thislist.pop(0)
# print(thislist) # ['banana', 'cherry']


# thislist = ["apple", "banana", "cherry"]
# thislist.pop()
# print(thislist) # ['apple', 'banana']


# thislist = ["apple", "banana", "cherry"]
# del thislist[0]
# print(thislist) # ['banana', 'cherry']


# thislist = ["apple", "banana", "cherry"]
# thislist.clear()
# print(thislist) # []


# thislist = ["apple", "banana", "cherry"]
# for x in thislist:
#     print(x)

# apple
# banana
# cherry


# thislist = ["apple", "banana", "cherry"]
# for i in range(len(thislist)):
#     print(thislist[i])

# apple
# banana
# cherry


# thislist = ["apple", "banana", "cherry"]
# i = 0
# while i < len(thislist):
#   print(thislist[i])
# #   print(i)
#   i = i + 1


# thislist = ["apple", "banana", "cherry"]
# [print(x) for x in thislist]

# apple
# banana
# cherry


# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []

# for x in fruits:
#   if "a" in x:
#     newlist.append(x)

# print(newlist) # ['apple', 'banana', 'mango']


# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = [x for x in fruits if "a" in x]
# print(newlist) # ['apple', 'banana', 'mango']


# newlist = [expression for item in iterable if condition == True]


# fruits = ["apple", "banana", "cherry", "kiwi", "mango", "apple", "apple",]
# newlist = [x for x in fruits if x != "apple"]
# print(newlist) # ['banana', 'cherry', 'kiwi', 'mango']


# newlist = [x for x in range(10)]
# print(newlist)


# newlist = [x for x in range(10) if x < 5]
# print(newlist) # [0, 1, 2, 3, 4]


# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = [x.upper() for x in fruits]
# print(newlist) # ['APPLE', 'BANANA', 'CHERRY', 'KIWI', 'MANGO']


# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = ['hello' for x in fruits]
# print(newlist) # ['hello', 'hello', 'hello', 'hello', 'hello']


# fruits = ["apple", "banana", "cherry", "kiwi", "mango", "banana", "banana",]
# newlist = [x if x != "banana" else "orange" for x in fruits]
# print(newlist) # ['apple', 'orange', 'cherry', 'kiwi', 'mango', 'orange', 'orange']


# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort()
# print(thislist)  # ['banana', 'kiwi', 'mango', 'orange', 'pineapple']


# thislist = [100, 50, 65, 82, 23]
# thislist.sort()
# print(thislist) # [23, 50, 65, 82, 100]


# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort(reverse = True)
# print(thislist)  # ['pineapple', 'orange', 'mango', 'kiwi', 'banana']


# thislist = [100, 50, 65, 82, 23]
# thislist.sort(reverse = True)
# print(thislist) # [100, 82, 65, 50, 23]


# def myfunc(n):
#   return abs(n - 50)

# thislist = [100, 50, 65, 82, 23]
# thislist.sort(key = myfunc)
# print(thislist) # [50, 65, 23, 82, 100]


# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.sort()
# print(thislist) # ['Kiwi', 'Orange', 'banana', 'cherry']


# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.sort(key = str.lower)
# print(thislist) # ['banana', 'cherry', 'Kiwi', 'Orange']

# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.sort(key = str.lower, reverse=True)
# print(thislist) # ['Orange', 'Kiwi', 'cherry', 'banana']


# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.sort(key = str.lower)
# thislist.reverse()
# print(thislist) # # ['Orange', 'Kiwi', 'cherry', 'banana']


# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist = [x.lower() for x in thislist]
# thislist.sort()
# print(thislist)  # ['banana', 'cherry', 'kiwi', 'orange']


# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.reverse()
# print(thislist) # ['cherry', 'Kiwi', 'Orange', 'banana']


# thislist = ["apple", "banana", "cherry"]
# mylist = thislist.copy()
# print(mylist) # ["apple", "banana", "cherry"]
# print(thislist == mylist) # True
# print(thislist is mylist) # False


# thislist = ["apple", "banana", "cherry"]
# mylist = list(thislist)
# print(mylist) # ["apple", "banana", "cherry"]
# print(thislist == mylist) # True
# print(thislist is mylist) # False


# thislist = ["apple", "banana", "cherry"]
# mylist = thislist[:]
# print(mylist) # ["apple", "banana", "cherry"]
# print(thislist == mylist) # True
# print(thislist is mylist) # False


# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]

# list3 = list1 + list2
# print(list3)  # ['a', 'b', 'c', 1, 2, 3]





# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]

# for x in list2:
#     list1.append(x)

# print(list1) # ['a', 'b', 'c', 1, 2, 3]



# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]

# list1.extend(list2)
# print(list1)  # ['a', 'b', 'c', 1, 2, 3]



# list1 = ["a", "b" , "c"]
# list2 = (1, 2, 3)

# list1.extend(list2)
# print(list1)  # ['a', 'b', 'c', 1, 2, 3]



# fruits = [ 'cherry', 'apple',  'cherry', 'banana', 'cherry', 'cherry',]
# x = fruits.count("cherry")
# print(x)  # 4


# fruits = ['apple', 'banana', 'cherry', 'cherry', 'cherry']
# x = fruits.index("cherry")
# print(x) # 2

# fruits = ['apple', 'banana', 'cherry', 'cherry', 'cherry']
# x = fruits.index("cherry")
# print(x) # 2



# fruits = [4, 55, 64, 32, 16, 32]
# x = fruits.index(32)
# print(x) # 3


# fruits = ['apple', 'banana', 'cherry', 'kiwi',  'mango', 'orange', 'cherry']
# x = fruits.index("cherry", 1)
# print(x) # 6


# fruits = ['apple', 'banana', 'cherry']
# fruits.insert(1, "orange")
# print(fruits) # ['apple', 'orange', 'banana', 'cherry']



