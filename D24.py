# DAY 24

# 100. You are given words. Some words may repeat. For each word, output its number of occurrences. The output order should correspond with the input order of appearance of the word. See the sample input/output for clarification.
# If the following string is given as input to the program:

# 4
# bcdef
# abcdefg
# bcde
# bcdef
# Then, the output of the program should be:

# 3
# 2 1 1

# Hints
# Make a list to get the input order and a dictionary to count the word frequency

# METHOD 1 (Mine)
n = int(input())

word_list = []
word_dict = {}

for i in range(n):
    word = input()
    if word not in word_dict:
        word_list.append(word)
    word_dict[word] = word_dict.get(word, 0) + 1

print(len(word_list))
for word in word_list:
    print(word_dict[word], end=' ')



# 101. You are given a string.Your task is to count the frequency of letters of the string and print the letters in descending order of frequency.
# If the following string is given as input to the program:

# aabbbccde
# Then, the output of the program should be:

# b 3
# a 2
# c 2
# d 1
# e 1
# Hints
# Count frequency with dictionary and sort by Value from dictionary Items

# METHOD 1 (SEEN)
word = input()
dct = {}
for i in word:
    dct[i] = dct.get(i,0) + 1

dct = sorted(dct.items(),key=lambda x: (-x[1],x[0]))
for i in dct:
    print(i[0],i[1])

# METHOD 2 (SEEN)
# X = input()
# my_set = set(X)
# arr = []
# for item in my_set:
#     arr.append([item,X.count(item)])
# tmp = sorted(arr,key = lambda x: (-x[1],x[0]))

# for i in tmp:
#     print(i[0]+' '+str(i[1]))



# 102. Write a Python program that accepts a string and calculate the number of digits and letters.
# Input

# Hello321Bye360
# Output

# Digit - 6
# Letter - 8
# Hints
# Use isdigit() and isalpha() function

# METHOD 1 (SEEN)
word = input()
digit,letter = 0,0
for char in word:
    digit+=char.isdigit()
    letter+=char.isalpha()

print('Digit -',digit)
print('Letter -',letter)



# 103. Given a number N.Find Sum of 1 to N Using Recursion
# Input

# 5
# Output

# 15
# Hints
# Make a recursive function to get the sum

# METHOD 1 (SEEN)
def rec(n):
    if n == 0:
        return n
    return rec(n-1) + n

n = int(input())
sum = rec(n)
print(sum)