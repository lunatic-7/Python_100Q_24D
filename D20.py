# DAY 20

# 80. Please write a program to print the list after removing even numbers in [5,6,77,45,22,12,24].

# METHOD 1 (Mine)
import enum
from operator import index


li = [5,6,77,45,22,12,24]
odd = [_ for _ in li if _ % 2 != 0]
print(odd)

# METHOD 2 (Alternate)
# odd_2 = list(filter(lambda x : x % 2 != 0, li))
# print(odd_2)



# 81. By using list comprehension, please write a program to print the list after removing numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155].

# METHOD 1 (Mine)
li_2 = [12,24,35,70,88,120,155]

div = [_ for _ in li_2 if _ % 35 != 0]
print(div)

# METHOD 2 (Alternate)
# div_2 = list(filter(lambda x : x % 35 != 0, li_2))
# print(div_2)



# 82. By using list comprehension, please write a program to print the list after removing the 0th, 2nd, 4th,6th numbers in [12,24,35,70,88,120,155].

# METHOD 1 (SEEN)
li_3 = [12,24,35,70,88,120,155]

enu = [x for i,x in enumerate(li_3) if i % 2 != 0 and i <= 6]  # enumerate() gives a tuple of (index,value)
print(enu)



# 83. By using list comprehension, please write a program to print the list after removing the 2nd - 4th numbers in [12,24,35,70,88,120,155].

# METHOD 1 (Mine)
li_4 = [12,24,35,70,88,120,155]
enu_2 = [x for i,x in enumerate(li_4) if i != 2 and i != 4]
print(enu_2)



# 84. By using list comprehension, please write a program generate a 3*5*8 3D array whose each element is 0.

# METHOD 1 (SEEN)
import pprint  # Just to get output in pretty way.
array = [[ [0 for col in range(8)] for col in range(5)] for row in range(3)]
pprint.pprint(array)