# myset = {"apple", "banana", "cherry"}
# print(myset) #  {'cherry', 'apple', 'banana'}


# myset = set(("apple", "banana", "cherry"))# note the double round-brackets
# print(myset) # {'cherry', 'apple', 'banana'}


# thisset = {"apple", "banana", "cherry", True, 1, "banana",}
# print(thisset) # {'cherry', 'apple', 'banana'}


# thisset = {"apple", "banana", "cherry", False, True, 0}
# print(thisset) # {False, True, 'apple', 'cherry', 'banana'}


# thisset = {"apple", "banana", "cherry"}
# print(len(thisset)) # 3


# set1 = {"apple", "banana", "cherry"}
# set2 = {1, 5, 7, 9, 3}
# set3 = {True, False, False}


# myset = {"apple", "banana", "cherry"}
# print(type(myset)) #  <class 'set'>


# thisset = {"apple", "banana", "cherry"}

# for x in thisset:
#   print(x)

# # cherry
# # banana
# # apple


# thisset = {"apple", "banana", "cherry"}
# print("banana" in thisset) # True


# thisset = {"apple", "banana", "cherry"}
# print("banana" not in thisset) # False
# print("watermelon" not in thisset) # True


# thisset = {"apple", "banana", "cherry"}
# thisset.add("orange")
# print(thisset) #  {'cherry', 'banana', 'apple', 'orange'}

# thisset.add("cherry")
# print(thisset) #  {'cherry', 'banana', 'apple', 'orange'}


# thisset = {"apple", "banana", "cherry"}
# tropical = {"pineapple", "mango", "papaya", "banana"}
# thisset.update(tropical)
# print(thisset) # {'mango', 'cherry', 'pineapple', 'papaya', 'banana', 'apple'}


# thisset = {"apple", "banana", "cherry"}
# mylist = ["kiwi", "orange"]
# thisset.update(mylist)
# print(thisset) # {'banana', 'apple', 'orange', 'cherry', 'kiwi'}


# thisset = {"apple", "banana", "cherry"}
# thisset.remove("banana")
# print(thisset) # {'apple', 'cherry'}


# thisset = {"apple", "banana", "cherry"}
# thisset.remove("kiwi")
# print(thisset) # error


# thisset = {"apple", "banana", "cherry"}
# thisset.discard("banana")
# print(thisset) # {'apple', 'cherry'}


# thisset = {"apple", "banana", "cherry"}
# thisset.discard("kiwi")
# print(thisset) # {'apple', 'cherry', 'banana'}


# thisset = {"apple", "banana", "cherry"}
# x = thisset.pop() # random item
# print(x) # random item
# print(thisset) # random item


# thisset = {"apple", "banana", "cherry"}
# thisset.clear()
# print(thisset) # set()


# thisset = {"apple", "banana", "cherry"}
# del thisset
# print(thisset) # NameError: name 'thisset' is not defined


# thisset = {"apple", "banana", "cherry"}
# for x in thisset:
#   print(x)

# # cherry
# # banana
# # apple


# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}

# set3 = set1.union(set2) # {1, 2, 3, 'b', 'c', 'a'}
# set3 = set1.update(set2) # None
# print(set3)


# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}

# set3 = set1 | set2
# print(set3) # {1, 2, 3, 'b', 'c', 'a'}


# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# set3 = {"John", "Elena"}
# set4 = {"apple", "bananas", "cherry"}

# myset = set1.union(set2, set3, set4) # {1, 2, 'b', 3, 'John', 'cherry', 'apple', 'Elena', 'c', 'a', 'bananas'}
# print(set1)
# print(myset) # {1, 2, 'b', 3, 'John', 'cherry', 'apple', 'Elena', 'c', 'a', 'bananas'}


# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# set3 = {"John", "Elena"}
# set4 = {"apple", "bananas", "cherry"}

# myset = set1 | set2 | set3 |set4
# print(myset) # {1, 2, 'b', 3, 'John', 'cherry', 'apple', 'Elena', 'c', 'a', 'bananas'}


# x = {"a", "b", "c"}
# y = (1, 2, 3)

# # z = x.union(y) # {1, 2, 'c', 3, 'a', 'b'}
# z = x | y # Error different type
# print(z)


# set1 = {"a", "b" , "c"}
# set2 = {1, 2, 3}

# set1.update(set2)
# print(set1) # {1, 2, 3, 'b', 'c', 'a'}


# set1 = {"apple", "banana", "cherry", 'google'}

# set2 = {"google", "microsoft", "apple"}

# set3 = set1.intersection(set2)
# print(set3) # {'google', 'apple'}
# print(set1) # {"apple", "banana", "cherry", 'google'}


# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set3 = set1 & set2
# print(set3)  # {'apple'}


# x = {"a", "b", "c"}
# y = ("a", "b", "c")

# z = x.intersection(y)
# z = x & y # Error different type
# print(z)


# set1 = {"apple", "banana", "cherry", "google"}
# set2 = {"google", "microsoft", "apple"}

# set1.intersection_update(set2) # {'google', 'apple'}
# set1.intersection().update(set2) # is not work

# print(set1)


# set1 = {"apple", 1,  "banana", 0, "cherry"}
# set2 = {False, "google", True, "apple", 2, 1}

# set3 = set1.intersection(set2)  # {False, True, 'apple'}
# set3 = set2.intersection(set1) # {0, 1, 'apple'}

# print(set3)


# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set3 = set1.difference(set2)  # {'banana', 'cherry'}
# set3 = set2.difference(set1) # {'google', 'microsoft'}

# print(set3)


# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set3 = set1 - set2 # {'banana', 'cherry'}
# set3 = set2 - set1 # {'google', 'microsoft'}

# print(set3)


# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set1.difference_update(set2)
# print(set1) # {'banana', 'cherry'}
# set2.difference_update(set1)
# print(set2) # {'google', 'microsoft'}


# ------------------------ запись заново -----------------------------------


# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set3 = set1.symmetric_difference(set2) # {'banana', 'google', 'microsoft', 'cherry'}
# set3 = set1.union(set2) # {'apple', 'cherry', 'banana', 'microsoft', 'google'}
# print(set3)


# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set3 = set1 ^ set2
# print(set3) # {'microsoft', 'banana', 'google', 'cherry'}


# set1 = {"apple", "banana", "cherry"}
# set2 = ("google", "microsoft", "apple")


# set1.symmetric_difference_update(set2)
# print(set1) # {'banana', 'microsoft', 'google', 'cherry'}
# set3 = set1 ^ set2 # # Error different type
# print(set3)


# x = frozenset({"apple", "banana", "cherry"})
# print(x)
# print(type(x)) # <class 'frozenset'>


# fs = frozenset({1, 2, 3})
# cp = fs.copy()
# print(fs)  # frozenset({1, 2, 3})
# print(cp)  # frozenset({1, 2, 3})


# a = frozenset({1, 2, 3, 4, 6})
# b = frozenset({3, 4, 5})
# print(a.difference(b)) # frozenset({1, 2})
# print(a - b) # frozenset({1, 2})



# a = frozenset({1, 2, 3, 4})
# b = frozenset({3, 4, 5})
# print(a.intersection(b)) #   frozenset({3, 4})
# print(a & b) # frozenset({3, 4})




# a = frozenset({1, 2})
# b = frozenset({3, 4})
# c = frozenset({2, 3})

# print(a.isdisjoint(b)) # True
# print(a.isdisjoint(c)) # False



# a = frozenset({1, 2})
# b = frozenset({1, 2})

# print(a.issubset(b)) # True
# print(a <= b) # True
# print(a < b) # False



# a = frozenset({1, 2})
# b = frozenset({1, 2})
# print(a.issuperset(b)) # True
# print(a >= b) # True
# print(a > b) # False



# a = frozenset({1, 2, 3})
# b = frozenset({3, 4, 5})
# print(a.symmetric_difference(b)) # frozenset({1, 2, 4, 5})
# print(a ^ b) # frozenset({1, 2, 4, 5})



# a = frozenset({1, 2})
# b = frozenset({2, 3})
# print(a.union(b)) # frozenset({1, 2, 3})
# print(a | b) # frozenset({1, 2, 3})





# my_set = {1, 2, 3}
# my_set.add(4)
# print(my_set)  # Вывод: {1, 2, 3, 4}


# my_set.remove(1)
# print(my_set)  # Вывод: {2, 3, 4}



# my_frozenset = frozenset([1, 2, 3])

# # Попытка изменить вызовет ошибку:
# my_frozenset.add(4) 
# print(my_frozenset)
# AttributeError: 'frozenset' object has no attribute 'add'




# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}

# x.update(y)
# z =  x.union(y)

# print(z) # {'apple', 'microsoft', 'banana', 'google', 'cherry'}
# print(x) # {'apple', 'microsoft', 'banana', 'google', 'cherry'}
