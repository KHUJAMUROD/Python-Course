# txt = "hello, and welcome to my world."
# x = txt.capitalize()
# print (x) # Hello, and welcome to my world.

# txt = "python is FUN!"
# x = txt.capitalize()
# print (x) # Python is fun!


# txt = "36 is my age."
# x = txt.capitalize()
# print (x) # 36 is my age.


# txt = "Hello, And Welcome To My World!"
# x = txt.casefold()
# print(x) # hello, and welcome to my world!


# print("Straße".lower())  # error
# print("Straße".casefold())  # Результат: 'strasse'

# text = "Maſter"
# print(text.lower())
# Результат: 'maſter' (сохранился символ 'ſ')
# print(text.casefold())
# Результат: 'master' (превратилось в стандартную 's')


# txt = "banana"
# x = txt.center(20)
# print(x) # '       banana       '

# txt = "banana"
# x = txt.center(20, "-")
# print(x) # -------banana-------


# txt = "I love apples, apple are my favorite fruit"
# x = txt.count("apple")
# print(x) # 2


# txt = "I love apples, apple are my favorite fruit"
# x = txt.count("apple", 10, 24)
# print(x) # 1


# txt = "My name is Ståle"
# x = txt.encode()
# print(x)


# txt = "My name is Ståle"

# print(txt.encode(encoding="ascii",errors="backslashreplace"))
# print(txt.encode(encoding="ascii",errors="ignore"))
# print(txt.encode(encoding="ascii",errors="namereplace"))
# print(txt.encode(encoding="ascii",errors="replace"))
# print(txt.encode(encoding="ascii",errors="xmlcharrefreplace"))

# txt = "Hello, welcome to my world."
# x = txt.endswith(".") # True
# x = txt.endswith(",") # False
# print(x)

# txt = "Hello, welcome to my world."
# x = txt.endswith("my world.") # True
# print(x)

# txt = "Hello, welcome to my world."
# x = txt.endswith("my world.", 5, 11) # False
# x = txt.endswith("my world.", 5) # True
# print(x)


# txt = "Hello, welcome to my castle."
# x = txt.endswith(("world.", "castle.")) # True
# x = txt.endswith(("world.", "castle.")) # True
# print(x)


# txt = "H\te\tl\tl\to"
# txt = "Hello"

# print(txt) # 'H	 e	l	l	o'
# print(txt.expandtabs()) # 'H       e       l       l       o'
# print(txt.expandtabs(2)) # 'H e l l o'
# print(txt.expandtabs(4)) # 'H   e   l   l   o'
# print(txt.expandtabs(10)) # 'H         e         l         l         o'


# txt = "Hello, welcome to my world."
# x = txt.find("welcome")
# print(x)


# txt = "Hello, welcome to my world."

# print(txt.find("q")) # -1
# print(txt.index("q")) # error not found


# txt = "For only {price:.2f} dollars!"
# print(txt.format(price = 49)) # For only 49.00 dollars!


# txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
# txt2 = "My name is {0}, I'm {1}".format("John",36)
# txt3 = "My name is {}, I'm {}".format("John",36)


# print(txt1) # My name is John, I'm 36
# print(txt2) # My name is John, I'm 36
# print(txt3) # My name is John, I'm 36


# txt = "Company12"
# x = txt.isalnum()
# print(x) # True


# txt = "Company 12"
# txt = "Company*&^%&^%"
# x = txt.isalnum()
# print(x) # False


# txt = "CompanyX"
# txt = "CompanyX123" # => False
# x = txt.isalpha()
# print(x) # True


# txt = "Company123"  # => True
# txt = "Компания123" # => False
# x = txt.isascii()
# print(x)


# txt = "1234" # => True
# txt = "abcd" # => False
# x = txt.isdecimal()
# print(x)

# txt = "50800"  # True
# txt = "50800.00"  # False
# x = txt.isdigit()
# print(x)


# a = "MyFolder"
# b = "Demo002"
# c = "2bring"
# d = "my demo"

# print(a.isidentifier()) # True
# print(b.isidentifier()) # True
# print(c.isidentifier()) # False
# print(d.isidentifier()) # False


# txt = "hello world!" # True
# txt = "hellO world!" # False
# x = txt.islower()
# print(x)


# a = "Hello world!" # False
# b = "hello 123" # True
# c = "mynameisPeter" # False

# print(a.islower())
# print(b.islower())
# print(c.islower())

# a = "\u0030" #unicode for 0
# b = "\u00B2" #unicode for &sup2;
# c = "10km2"
# d = "-1"
# e = "1.5"
# f = '1235345'

# print(a.isnumeric()) # True
# print(b.isnumeric()) # True
# print(c.isnumeric()) # False
# print(d.isnumeric()) # False
# print(e.isnumeric()) # False
# print(f.isnumeric()) # True


# txt = "Hello! Are you #1?" # True
# x = txt.isprintable()
# print(x)


# txt = "Hello!\nAre you #1?" # False
# txt = "Hello!\tAre you #1?"  # False
# txt = "Hello!\"Are you #1?"  # True
# x = txt.isprintable()
# print(x)


# txt = "   " # True
# x = txt.isspace()
# print(x)


# txt = "   s   " # False
# txt = "   5   " # False
# x = txt.isspace()
# print(x)


# txt = "Hello, And Welcome To My World!" # True
# txt = "Hello, And Welcome To My world!" # False
# x = txt.istitle()
# print(x)

# a = "HELLO, AND WELCOME TO MY WORLD"
# b = "Hello"
# c = "22 Names"
# d = "This Is %'!?"

# print(a.istitle()) # False
# print(b.istitle()) # True
# print(c.istitle()) # True
# print(d.istitle()) # True


# txt = "THIS IS NOW!"  # True
# x = txt.isupper()
# print(x)


# a = "Hello World!"
# b = "hello 123"
# c = "MY NAME IS PETER"

# print(a.isupper()) # False
# print(b.isupper()) # False
# print(c.isupper()) # True


# myTuple = ("John", "Peter", "Vicky")
# x = "#".join(myTuple)
# print(x) # John#Peter#Vicky
# x = "----".join(myTuple)
# print(x) # John----Peter----Vicky


# myDict = {"name": "John", "country": "Norway"}
# mySeparator = "__---___"
# x = mySeparator.join(myDict)
# print(x) # name__---___country


# txt = "Hello my FRIENDS"
# x = txt.lower()
# print(x) # hello my friends


# txt = "banana"
# x = txt.ljust(20)
# print(x, "is my favorite fruit.") # 'banana               is my favorite fruit.'


# txt = "     banana     "
# x = txt.lstrip()
# print("of all fruits", x, "is my favorite") # of all fruits banana      is my favorite


# txt = ",,,,,ssaaww.....banana,,,,,ssaaww....."
# x = txt.lstrip(",.asw")
# print(x) # banana,,,,,ssaaww.....



# txt = "Hello Sam!"
# mytable = str.maketrans("S", "P")
# print(txt.translate(mytable)) # Hello Pam!


# txt = "Hi Sam! aSmS"
# x = "mSa"
# y = "eJo"

# mytable = str.maketrans(x, y)
# print(txt.translate(mytable)) # Hi Joe! oJeJ


# Третий параметр в таблице соответствия описывает символы, которые вы хотите удалить из строки:
# txt = "Good night Sam!" 
# x = "mSa"
# y = "eJo"
# z = "odnght"
# mytable = str.maketrans(x, y, z)
# print(txt.translate(mytable))


# txt = "I could eat bananas all day"
# x = txt.partition("bananas")
# print(x) # ('I could eat ', 'bananas', ' all day')


# txt = "I could eat bananas all day"
# x = txt.partition("apples")
# print(x) # ('I could eat bananas all day', '', '')



# txt = "I like bananas"
# x = txt.replace("bananas", "apples")
# print(x) # I like apples


# txt = "one one was a race horse, two two was one too."
# x = txt.replace("one", "three")
# print(x) # three three was a race horse, two two was three too.


# txt = "one one was a race horse, two two was one too."
# x = txt.replace("one", "three", 2)
# print(x) # three three was a race horse, two two was one too.



# txt = "Mi casa, su casa."
# x = txt.rfind("casa") # 12
# x = txt.find("casa") # 3
# print(x)



# txt = "Hello, welcome to my world."
# x = txt.rfind("e", 5, 10) # 8
# x = txt.rfind("e",) # 13
# x = txt.rfind("e", 0, 5) # 1
# print(x) 


# txt = "Hello, welcome to my world."

# print(txt.rfind("q")) # -1
# print(txt.rindex("q")) # error


# txt = "banana"
# x = txt.rjust(20) # '              banana is my favorite fruit.'
# print(x, "is my favorite fruit.") 



# txt = "banana"
# x = txt.rjust(20, "-")  # --------------banana
# print(x)

# txt = "I could eat bananas all day, bananas are my favorite fruit"
# x = txt.rpartition("bananas") 
# print(x) # ('I could eat bananas all day, ', 'bananas', ' are my favorite fruit')



# txt = "I could eat bananas all day, bananas are my favorite fruit"
# x = txt.rpartition("apples")
# print(x)  # ('', '', 'I could eat bananas all day, bananas are my favorite fruit')



# txt = "apple, banana, cherry"
# x = txt.rsplit(", ")  # # ['apple', 'banana', 'cherry']
# x = txt.split(", ") # # ['apple', 'banana', 'cherry']
# print(x) 


# txt = "apple, banana, cherry"

# setting the maxsplit parameter to 1, will return a list with 2 elements!
# x = txt.rsplit(", ", 1) # ['apple, banana', 'cherry']
# x = txt.split(", ", 1) # ['apple', 'banana, cherry']
 
# print(x)



# txt = "hello, my name is Peter, I am 26 years old"
# x = txt.split(", ")
# print(x) # ['hello', 'my name is Peter', 'I am 26 years old']


# txt = "apple#banana#cherry#orange"
# x = txt.split("#") # ['apple', 'banana', 'cherry', 'orange']
# print(x)


# txt = "apple#banana#cherry#orange"
# setting the maxsplit parameter to 1, will return a list with 2 elements!
# x = txt.split("#", 1) # ['apple', 'banana#cherry#orange']
# print(x)


# txt = "Thank you for the music\nWelcome to the jungle"
# txt = "Thank you for the musicWelcome to the jungle"
# x = txt.splitlines() # ['Thank you for the music', 'Welcome to the jungle']
# print(x) 


# txt = "Thank\nyoufor\nthemusic\nWelcome to\n the jungle"
# # x = txt.splitlines(True) # ['Thank\n', 'youfor\n', 'themusic\n', 'Welcome to\n', ' the jungle']
# # x = txt.splitlines() # ['Thank', 'youfor', 'themusic', 'Welcome to', ' the jungle']
# print(x)



# txt = "Hello, welcome to my world."
# x = txt.startswith("Hello") # True
# print(x)


# txt = "Hello, welcome to my world."
# x = txt.startswith("wel", 7, 20) # True
# print(x)



# txt = "Hi, welcome to my world." # True
# txt = "Hello, welcome to my world." # True
# x = txt.startswith(("Hello", "Hi"))
# print(x)



# txt = "     banana     "

# x = txt.strip() # of all fruits banana is my favorite
# print("of all fruits", x, "is my favorite")

# y = txt # of all fruits      banana      is my favorite
# print("of all fruits", y, "is my favorite")



# txt = "Hello My Name Is PETER"
# x = txt.swapcase() # hELLO mY nAME iS peter
# print(x)



# txt = "Welcome to my world"
# x = txt.title() # Welcome To My World
# print(x)


# txt = "Welcome to my 2nd world"
# x = txt.title() # Welcome To My 2Nd World
# print(x) 



# txt = "hello b2b2b2 a%nd 3g3g3g"
# x = txt.title()  # Hello B2B2B2 A%Nd 3G3G3G
# print(x) 


# txt = "Hello my friends"
# x = txt.upper() # HELLO MY FRIENDS
# print(x)

# txt = "50" # 0000000050
# txt = "abcd" # 000000abcd
# x = txt.zfill(10)
# print(x)


# a = "hello"
# b = "welcome to the jungle"
# c = "10.000"

# print(a.zfill(10)) # 00000hello
# print(b.zfill(10)) # welcome to the jungle
# print(c.zfill(10)) # 000010.000