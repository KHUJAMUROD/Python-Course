# thisdict1 = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# print(thisdict1)

# thisdict2 = dict(
#   brand = "Ford",
#   model = "Mustang",
#   year1 = 1964,
#   year2 = 1964
# #   year1 = 1964 # error
# )

# print(thisdict2)


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict["brand"]) # "Ford"

# print(thisdict.brand) // error
# print(len(thisdict)) # 3


# thisdict = {
#   "brand": "Ford",
#   "electric": False,
#   "year": 1964,
#   "colors": ["red", "white", "blue"]
# }


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(type(thisdict))  # <class 'dict'>


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x1 = thisdict["model"]
# x2 = thisdict.get("model")

# print(x1) # "Mustang"
# print(x2) # "Mustang"


# x = thisdict.keys()
# print(x) # dict_keys(['brand', 'model', 'year'])
# print(type(x)) # <class 'dict_keys'>


# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }

# x = car.keys()

# print(x) #before the change # dict_keys(['brand', 'model', 'year'])

# car["color"] = "white"

# print(x) #after the change # dict_keys(['brand', 'model', 'year', 'color'])

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# # x = thisdict.values()
# # print(x) # dict_values(['Ford', 'Mustang', 1964])
# # print(type(x)) # <class 'dict_values'>


# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }

# x = car.values()

# print(x) #before the change # dict_values(['Ford', 'Mustang', 1964])

# car["color"] = "red"

# print(x) #after the change # dict_values(['Ford', 'Mustang', 1964, 'red'])


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# x = thisdict.items()
# print(x) # dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])


# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }

# x = car.items()
# print(x) #before the change # dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])

# car["year"] = 2020
# print(x) #after the change # dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 2020)])


# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }

# x = car.items()
# print(x) #before the change # dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])
# car["color"] = "red"
# print(x) #after the change # dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964), ('color', 'red')])


# thisdict = {
#     # "model": "BMW",
#     "brand": "Ford",
#     "model1": "model",
#     "year": 1964
# }


# if "model" in thisdict:
#     print("Yes, 'model' is one of the keys in the thisdict dictionary")
# else:
#     print("No, 'model' is not one of the keys in the thisdict dictionary")


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict["year"] = 2018
# print(thisdict) # {'brand': 'Ford', 'model': 'Mustang', 'year': 2018}


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict) # {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
# thisdict.update({"year": 2020})

# print(thisdict) # {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.pop() # error
# print(thisdict)

# thisdict.pop("model")
# print(thisdict)  # {'brand': 'Ford', 'year': 1964}


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.popitem() # delete last item
# print(thisdict) # {'brand': 'Ford', 'model': 'Mustang'}


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }


# del thisdict["model"]
# print(thisdict)  # {'brand': 'Ford', 'year': 1964}


# del thisdict # deleted all dict
# print(thisdict)  # is not defined


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.clear()
# print(thisdict) # {}


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# for x in thisdict:
#   print(x)

# # brand
# # model
# # year


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# for x in thisdict:
#   print(thisdict[x])

# Ford
# Mustang
# 1964


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# for x in thisdict:
#   print(x, thisdict[x])

# # brand Ford
# # model Mustang
# # year 1964


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }


# for x in thisdict.values():
#   print(x)


# Ford
# Mustang
# 1964


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# for x in thisdict.keys():
#   print(x)


# brand
# model
# year


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }


# for x, y in thisdict.items():
#   print(x, y)


# brand Ford
# model Mustang
# year 1964


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# mydict = thisdict # Not copy
# mydict = thisdict.copy()

# mydict["brand"] = 'Lexsus'
# print(thisdict)
# print(mydict)


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# mydict = dict(thisdict)

# mydict["brand"] = 'Lexsus'
# print(thisdict)
# print(mydict)


# myfamily = {
#   "child1" : {
#     "name" : "Emil",
#     "year" : 2004
#   },
#   "child2" : {
#     "name" : "Tobias",
#     "year" : 2007
#   },
#   "child3" : {
#     "name" : "Linus",
#     "year" : 2011
#   }
# }


# print(myfamily['child1']['name']) # Emil
# print(myfamily["child2"]["name"]) # Tobias
# print(myfamily["child3"]["year"]) # 2011


# myfamily = {
#     "child1": {
#         "name": "Emil",
#         "year": 2004
#     },
#     "child2": {
#         "name": "Tobias",
#         "year": 2007
#     },
#     "child3": {
#         "name": "Linus",
#         "year": 2011
#     }
# }


# print(list(myfamily.keys())[0])
# print(myfamily['child1']['name'])
# print(myfamily['child1']['year'])
# print(list(myfamily.keys())[1])
# print(myfamily['child2']['name'])
# print(myfamily['child3']['year'])
# print(list(myfamily.keys())[2])
# print(myfamily['child3']['name'])
# print(myfamily['child3']['year'])


# for x, obj in myfamily.items():
#     print(x)

#     for y in obj:
#         print(y + ':', obj[y])




# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# car.clear()

# print(car) # {}



# x = ('key1', 'key2', 'key3')
# y = 0

# thisdict = dict.fromkeys(x, y)
# print(thisdict) # {'key1': 0, 'key2': 0, 'key3': 0}




# x = ('key1', 'key2', 'key3')
# thisdict = dict.fromkeys(x)
# print(thisdict) # {'key1': None, 'key2': None, 'key3': None}




# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# x = car.get("model")
# print(x) # Mustang



# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# x = car.items()

# print(x)  # dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])




# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# x = car.keys() # dict_keys(['brand', 'model', 'year'])
# print(x)







# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# x = car.pop("model")


# print(car) # {'brand': 'Ford', 'year': 1964}
# print(x) # Mustang




# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# x = car.popitem()

# print(car) # {'brand': 'Ford', 'model': 'Mustang'}
# print(x) # ('year', 1964)


# car = {
#   "brand": "Ford",
# #   "model": "Mustang",
#   "year": 1964
# }
# # print(car['model']) # error

# x = car.setdefault("model", "Bronco")
# print(x) # Bronco
# print(car)  # {'brand': 'Ford', 'year': 1964, 'model': 'Bronco'}



# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# car.update({"color": "red"})
# car.update({"brand": "White"})

# print(car) # {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}




# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# x = car.values()

# print(x) # dict_values(['Ford', 'Mustang', 1964])


car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.values()

car["year"] = 2018

print(x) # dict_values(['Ford', 'Mustang', 2018])