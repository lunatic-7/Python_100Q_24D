# DAY 15

# 54. Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the company name of a given email address. Both user names and company names are composed of letters only.
# Example: If the following email address is given as input to the program:
# john@google.com
# Then, the output of the program should be:
# google

# METHOD 1 (Mine)
inp = input()
temp = inp.split(".")
temp2 = (temp[0].split("@"))
print(temp2[1])

# METHOD 2 (Alternate)
# import re

# email = "john@google.com elise@python.com"
# pattern = "\w+@(\w+).com"
# ans = re.findall(pattern,email)
# print(ans)



# 55. Write a program which accepts a sequence of words separated by whitespace as input to print the words composed of digits only.
# Example: If the following words is given as input to the program:
# 2 cats and 3 dogs.
# Then, the output of the program should be:
# ['2', '3']

# METHOD 1 (Mine)
pet = input().split(" ")
li = []
for _ in pet:
    if _.isdigit():
        li.append(_)

print(li)

# METHOD 2 (Alternate)
# import re

# email = input()
# pattern = "\d+"
# ans = re.findall(pattern,email)
# print(ans)



# 56. Print a unicode string "hello world".

# METHOD 1 (SEEN)
temporary = u"Hello World"
print(temporary)



# 57. Write a program to read an ASCII string and to convert it to a unicode string encoded by utf-8.

# METHOD 1 (SEEN)
s = input()
u = s.encode('utf-8')
print(u)



# 58. Write a special comment to indicate a Python source code file is in unicode.

# METHOD 1 (SEEN)
# -*- coding: utf-8 -*-



# 59. Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0).
# Example: If the following n is given as input to the program:
# 5
# Then, the output of the program should be:
# 3.55

# METHOD 1 (SEEN)
n = int(input())
sum = 0
for i in range(1, n+1):
    sum+= i/(i+1)
print(round(sum, 2))  # rounded to 2 decimal point
