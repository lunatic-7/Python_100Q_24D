# DAY 2

# 4. Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.Suppose the following input is supplied to the program:
# 34,67,55,33,12,98
# Then, the output should be:
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')

# METHOD 1 (Mine)
from cmath import sqrt


def comma_sep():  # num is no. of characters you want to store
    inp = input().split(",")  # split automatically return a list
    tup = tuple(inp)
    print(inp)
    print(tup)

comma_sep()



# 5. Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods. 

# METHOD 1 (Seen)
class inpPriStr():
    def get_string(self):
        self.s = input()
    
    def print_string(self):
        print(self.s.upper())

x = inpPriStr()
x.get_string()
x.print_string()



# 6. Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated sequence.For example Let us assume the following comma separated input sequence is given to the program:
# 100,150,180
# The output of the program should be:
# 18,22,24

# METHOD 1 (Mine)
from math import sqrt
C = 50
H = 30
def square(D):
    sq = sqrt((2 * C * D)/H)
    return round(sq)

D = input().split(",")

li = []
for _ in D:
    li.append(str(square(int(_))))
print(",".join(li)) # Join requires an iterable, eg, a list of strings

# METHOD 2 (Alternate)
# C, H = 50, 30
# mylist = input().split(',')
# print(*(round(sqrt(2*C*int(D)/H)) for D in mylist), sep=",")



# 7. _Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i * j.
# Note: i=0,1.., X-1; j=0,1,¡­Y-1. Suppose the following inputs are given to the program: 3,5
# Then, the output of the program should be:
# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

# METHOD 1 (Mine)
x, y = map(int,input().split(",")) # To take values to x and y in comma seperated manner and convert them in int, using map function.
li = []
for i in range(x):
    tmp = []
    for j in range(y):
        temp = i*j
        tmp.append(temp)
    li.append(tmp)
print(li)

# METHOD 2 (Alternate)
# x,y = map(int,input().split(','))
# lst = [[i*j for j in range(y)] for i in range(x)]
# print(lst)



# 8. Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
# Suppose the following input is supplied to the program:
# without,hello,bag,world
# Then, the output should be:
# bag,hello,without,world

# METHOD 1 (Mine)
word = input().split(",")
li = sorted(word)
print(",".join(li))



# Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
# Suppose the following input is supplied to the program:
# Hello world
# Practice makes perfect
# Then, the output should be:
# HELLO WORLD
# PRACTICE MAKES PERFECT

# METHOD 1 (Mine)
s = ''
while 1:
    string = input()
    if len(string) == 0:
        break
    stri = string.upper()
    s += stri + "\n"
print(s)

# METHOD 2 (Alternate)
# lst = []
# while True:
#     x = input()
#     if len(x)==0:
#         break
#     lst.append(x.upper())

# for line in lst:
#     print(line)
