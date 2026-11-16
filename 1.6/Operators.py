# x = 5
# y = 3

# print(x + y)  # 8
# print(x - y)  # 2
# print(x * y)  # 15
# print(x ** y)  # 125
# print(x / y)  # 1.6666666666666667

# print(10 % 2)  # 0
# print(10 % 3)  # 1
# print(10 % 30)  # 10


# print(10 // 2)  # 5
# print(10 // 3)  # 3
# print(10 // 30)  # 0


# x = 5
# x += 10  # x = x + 10
# print(x)

# x = 2
# x *= 5 # x = x * 5
# print(x) # 10

# x = 20
# x /= 5 # x = x / 5
# print(x) # 4

# x = 20
# x -= 5 # x = x - 5
# print(x) # 15

# x = 5
# x **= 3 # x = x ** 3
# print(x) # 125

# x = 15
# x %= 4 # x = x % 4
# print(x) # 3

# x = 20
# x //= 4 # x = x // 4
# print(x) # 5


# print(bin(16)) # 0b10000

# print(16 / 2) # 0b0
# print(8 / 2) # 0b00
# print(4 / 2) # 0b000
# print(2 / 2) # 0b0000
# print(1 / 2) # 0b00001

# print(bin(463))  # 0b111001111

# print(463 / 2)  # 0b1
# print(231 / 2)  # 0b11
# print(115 / 2)  # 0b111
# print(57 / 2)   # 0b1111
# print(28 / 2)   # 0b11110
# print(14 / 2)   # 0b111100
# print(7 / 2)    # 0b1111001
# print(3 / 2)    # 0b11110011
# print(1 / 2)    # 0b111100111  => reverse = 0b111001111


# print(bin(6)) # 0b110
# print(bin(3)) # 0b011
# #             # 0b010
# #             # 0b01000

# print(0b01000) => 2 * 2 * 2 = 8
# print(6 & 3)


# print(bin(24)) # 0b11000
# print(bin(3))  # 0b00011
# #              # 0b00000

# print(24 & 3) # 0

# print(bin(36)) # 0b100100
# print(bin(28)) # 0b011100
# #              # 0b000100

# print(36 & 28) # 4

# print(bin(444)) # 0b110111100
# print(bin(77))  # 0b001001101
# #               # 0b000001100

# print(444 & 77) # 12


# print(bin(12)) # 0b1100
# print(bin(8)) #  0b1000
# #             #  0B1100  

# print(12 | 8) #  12


# print(bin(323)) # 0b101000011
# print(bin(44))  # 0b000101100
# #               # 0B101101111
# # 1 + 2 + 4 + 8 + 32 + 64 + 256 
# print(1 + 2 + 4 + 8 + 32 + 64 + 256 ) # 367
# print(323 | 44) #  367


# print(bin(323)) # 0b101000011
# print(bin(44))  # 0b000101100
# # #             # 0b101101111

# print(323 ^ 44) # 367


# print(bin(212)) # 0b11010100
# print(bin(33))  # 0b00100001
# #             # 0b11110101
# 1 + 4 + 16 + 32 + 64 + 128
# print(1 + 4 + 16 + 32 + 64 + 128) # 245
# print(212 ^ 33) # 245 



# ~x = -(x + 1)
# print(~505)
# print(bin(-506)) # 0b111111010
# print(bin(~505)) # 0b111111010


# print(bin(5)) # 0b101
# #             # 0b101000  
# # 2 ** 3 + 2 ** 5
# print(2 ** 3 + 2 ** 5) # 40
# print (5 << 3) # 40


# print(bin(10)) # 0b0001
# #              # 0b0001
# print (10 >> 3) # 1
# #              # 0b0010
# print (10 >> 2) # 2



# x = 5
# x &= 3
# print(x) # 1
# print(5 & 3) # 1

# x = 5
# x |= 3
# print(x) # 7
# print(5 | 3) # 7

# x = 5
# x ^= 3
# print(x) # 6
# print(5 ^ 3) # 6

# x = 52
# x >>= 3
# print(x) # 6
# print(52 >> 3) # 6

# x = 5
# x <<= 3
# print(x) # 40
# print(5 << 3) # 40


# x = ''
# print(x := 123) # 123
# print(x) # 123


# numbers = [1, 2, 3, 4, 5]

# if (count := len(numbers)) > 3:
#     print(f"List has {count} elements")

# print(count) # 5




# num = 6
# x = "WEEKEND!" if num > 5 else "Workday"
# print(x)


# num = 1

# x = "Fri" if num == 5 else "Sat" if num == 6 else "Sun" if num == 7 else "weekday"
# print(x)


# x = 5
# y = 3

# print(x == y)  # False
# print(x != y) # True
# print(x > y) # True
# print(x < y) # False
# print(x >= y) # True
# print(x <= y) # False



# x = 5
# print(1 < x < 10) # True


# print(1 > x and x < 10 and 123 and 777) # False


# print(1 > x or x < 10 or 0 or '') # True


# x = 5
# print(not(x > 3 and x < 10)) # False


# x = ["apple", "banana"]
# y = ["apple", "banana"]
# z = x

# print(x == y) # True
# print(x is y) # False
# print(x is z) # True

# print(x is not y) # True
# print(x is not z) # False



# fruits = ["apple", "banana", "cherry"]
# print("banana" in fruits) # True



# fruits = ["apple", "banana", "cherry"]
# print("pineapple" not in fruits) # True


# text = "Hello World"

# print("H" in text) # True
# print("hello" in text) # False
# print("z" not in text) # True

