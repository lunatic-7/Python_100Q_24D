# DAY 3

# 10. Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
# Suppose the following input is supplied to the program:
# hello world and practice makes perfect and hello world again
# Then, the output should be:
# again and hello makes perfect practice world

# METHOD 1 (Mine)
inp = input().split()
temp = sorted(set(inp))
print(" ".join(temp))

# METHOD 2 (Alternate)
# word = input().split()

# for i in word:
#     if word.count(i) > 1:    #count function returns total repeatation of an element that is send as argument
#         word.remove(i)     # removes exactly one element per call

# word.sort()
# print(" ".join(word))



# 11. Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
# Example:
# 0100,0011,1010,1001
# Then the output should be:
# 1010

# METHOD 1 (Mine)
li = []
num = input().split(",")
for _ in num:
    if (int(_,2) % 5 == 0):
        li.append(_)

print(",".join(li))

# METHOD 2 (Alternate)
# print(*(binary for binary in input().split(',') if int(binary,base=2)%5==0))



# 12. Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.The numbers obtained should be printed in a comma-separated sequence on a single line.

# METHOD 1 (Mine) Seen
# ASCII digits of even digits are also even.
lst = []

for i in range(1000,3001):
    flag = 1
    for j in str(i):          # every integer number i is converted into string
        if ord(j)%2 != 0:     # ord returns ASCII value and j is every digit of i
            flag = 0          # flag becomes zero if any odd digit found
    if flag == 1:
        lst.append(str(i))    # i is stored in list as string

print(",".join(lst))



# 13. Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3

# METHOD 1 (Mine)
digit, letter = 0, 0
st = input()
for _ in st:
    if _.isdigit():
        digit += 1
    if _.isalpha():
        letter += 1
print(f"LETTERS {letter}")
print(f"DIGITS {digit}")

# METHOD 2 (Alternate)
# word = input()
# letter,digit = 0,0

# for i in word:
#     if ('a'<=i and i<='z') or ('A'<=i and i<='Z'):
#         letter+=1
#     if '0'<=i and i<='9':
#         digit+=1

# print("LETTERS {0}\nDIGITS {1}".format(letter,digit))
