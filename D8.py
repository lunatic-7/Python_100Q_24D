# DAY 8

# 22. Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically.
# Suppose the following input is supplied to the program:
# New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
# Then, the output should be:
# 2:2
# 3.:1
# 3?:1
# New:1
# Python:5
# Read:1
# and:1
# between:1
# choosing:1
# or:2
# to:1

# METHOD 1 (Mine)
temp = input().split()
li = []
for _ in temp:
    li.append(f"{_}: {temp.count(_)}")
s = sorted(set(li))
for _ in s:
    print(_)

# METHOD 2 (Alternate)
# from pprint import pprint
# p=input().split()
# pprint({i:p.count(i) for i in p})



# 23. Write a method which can calculate square value of number

# METHOD 1 (MINE)
inp = int(input())
print(inp**2)


# 24. Python has many built-in functions, and if you do not know how to use it, you can read document online or find some books. But Python has a built-in document function for every built-in functions.
# Please write a program to print some Python built-in functions documents, such as abs(), int(), raw_input()
# And add document for your own function

# METHOD 1 (Mine)
print(str.__doc__)
print(sorted.__doc__)

def pow(n,p):
    '''
    param n: This is any integer number
    param p: This is power over n
    return:  n to the power p = n^p
    '''

    return n**p

print(pow(3,4))
print(pow.__doc__)

# 25. Define a class, which have a class parameter and have a same instance parameter.

# METHOD 1 (Mine)
class Car:
    name = "Car"

    def __init__(self,name = None):
        self.name = name

honda=Car("Honda")
print(f"{Car.name} name is {honda.name}")

toyota=Car()
toyota.name="Toyota"
print(f"{Car.name} name is {toyota.name}")