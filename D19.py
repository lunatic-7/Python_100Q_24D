# DAY 19

# 75. Please write a program to randomly print a integer number between 7 and 15 inclusive.

# METHOD 1 (Mine)
import random
print(random.randint(7,15))

# METHOD 2 (Alternate)
# print(random.randrange(7,16))



# 76. Please write a program to compress and decompress the string "hello world!hello world!hello world!hello world!".

# METHOD 1 (SEEN)
import zlib
s = 'hello world!hello world!hello world!hello world!'
# In Python 3 zlib.compress() accepts only DataType <bytes>
y = bytes(s, 'utf-8')
x = zlib.compress(y)
print(x)
print(zlib.decompress(x))



# 77. Please write a program to print the running time of execution of "1+1" for 100 times.

# METHOD 1 (SEEN)
import time

before = time.time()
print(before)
for i in range(100):
    x = 1 + 1
after = time.time()
print(after)
execution_time = after - before
print(execution_time)

# METHOD 2 (Alternate)
# import datetime

# before = datetime.datetime.now()
# for i in range(100):
#     x = 1 + 1
# after = datetime.datetime.now()
# execution_time = after - before
# print(execution_time.microseconds)



# 78. Please write a program to shuffle and print the list [3,6,7,8].

# METHOD 1 (Mine)
li = [3,6,7,8]
# BEFORE SHUFFLING
print(li)
random.shuffle(li)
# AFTER SHUFFLING
print(li)

# 79. Please write a program to generate all sentences where subject is in ["I", "You"] and verb is in ["Play", "Love"] and the object is in ["Hockey","Football"].

# METHOD 1 (Mine)
subject = ["I", "You"]
verb = ["Play", "Love"]
object = ["Hockey", "Football"]

for s in subject:
    for v in verb:
        for o in object:
            print(f"{s} {v} {o}")

# METHOD 2 (Alternate)
# import itertools
# subject = ["I", "You"]
# verb = ["Play", "Love"]
# objects = ["Hockey","Football"]

# sentence = [subject, verb, objects]
# n = list(itertools.product(*sentence))
# for i in n: 
#     print(i)