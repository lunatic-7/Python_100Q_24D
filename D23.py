# DAY 23

# 95. Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given scores. Store them in a list and find the score of the runner-up.
# If the following string is given as input to the program:
# 5
# 2 3 6 6 5
# Then, the output of the program should be:
# 5

# METHOD 1 (SEEN)

n = int(input())
arr = map(int, input().split())
arr = list(arr)
if len(arr) != n:
    print("Invalid Length!")
else:
    arr = list(set(arr))
    arr.sort()
    print(arr[-2]) 



# 96. You are given a string S and width W. Your task is to wrap the string into a paragraph of width.
# If the following string is given as input to the program:
# ABCDEFGHIJKLIMNOQRSTUVWXYZ
# 4
# Then, the output of the program should be:
# ABCD
# EFGH
# IJKL
# IMNO
# QRST
# UVWX
# YZ

# METHOD 1 (SEEN)
import textwrap

string = input()
width = int(input())

print(textwrap.fill(string,width))

# METHOD 2 (Alternate)
# from textwrap import wrap
# x = str(input())
# w = int(input())
# z = list(wrap(x, w))
# for i in z:
#     print(i)



# 97. You are given an integer, N. Your task is to print an alphabet rangoli of size N. (Rangoli is a form of Indian folk art based on creation of patterns.)
# Different sizes of alphabet rangoli are shown below:

# #size 3

# ----c----
# --c-b-c--
# c-b-a-b-c
# --c-b-c--
# ----c----

# #size 5

# --------e--------
# ------e-d-e------
# ----e-d-c-d-e----
# --e-d-c-b-c-d-e--
# e-d-c-b-a-b-c-d-e
# --e-d-c-b-c-d-e--
# ----e-d-c-d-e----
# ------e-d-e------
# --------e--------

# METHOD 1 (SEEN)
import string
def print_rangoli(size):
    n = size
    alph = string.ascii_lowercase  # Gives a string of all lowercase letters
    width = 4 * n - 3

    ans = []
    for i in range(n):
        left = '-'.join(alph[n - i - 1:n])
        mid = left[-1:0:-1] + left
        final = mid.center(width, '-') # The center(length, character) method will center align the string, using a specified character (space is default) as the fill character.

        ans.append(final)

    if len(ans) > 1:
        for i in ans[n - 2::-1]:
            ans.append(i)
    ans = '\n'.join(ans)
    print(ans)


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)



# 98. You are given a date. Your task is to find what the day is on that date.
# Input
# A single line of input containing the space separated month, day and year, respectively, in MM DD YYYY format.
# 08 05 2015
# Output
# Output the correct day in capital letters.
# WEDNESDAY

# METHOD 1 (SEEN)
import calendar

month, day, year = map(int, input().split())

dayId = calendar.weekday(year, month, day)
print(calendar.day_name[dayId].upper())



# 99. Given 2 sets of integers, M and N, print their symmetric difference in ascending order. The term symmetric difference indicates those values that exist in either M or N but do not exist in both.
# Input

# The first line of input contains an integer, M.The second line contains M space-separated integers.The third line contains an integer, N.The fourth line contains N space-separated integers.

# 4
# 2 4 5 9
# 4
# 2 4 11 12
# Output

# Output the symmetric difference integers in ascending order, one per line.

# 5
# 9
# 11
# 12

# Hints
# Use '^' to make symmetric difference operation.

# METHOD 1 (SEEN)
n = int(input())
set1 = set(map(int,input().split()))

m = int(input())
set2 = set(map(int, input().split()))

ans = list(set1 ^ set2)
ans.sort()
for i in ans:
    print(i)