# DAY 22

# 90. Please write a program which count and print the numbers of each character in a string input by console.
# Example: If the following string is given as input to the program:
# abcdefgabc
# Then, the output of the program should be:
# a,2
# c,2
# b,2
# e,1
# d,1
# g,1
# f,1

# METHOD 1 (Mine)
str = input()
li = []
for _ in str:
    li.append(f"{_},{str.count(_)}")
fin = set(li)
for _ in fin:
    print(_)

# METHOD 2 (Alternate)
# s = 'abcdefgabc'
# for i in sorted(set(s)):
#     print(f'{i}, {s.count(i)}')


# 91. Please write a program which accepts a string from console and print it in reverse order.
# Example: If the following string is given as input to the program:*
# rise to vote sir
# Then, the output of the program should be:
# ris etov ot esir

# METHOD 1 (Mine)
str_2 = input()
s = "".join(reversed(str_2))
print(s)

# METHOD 2 (Alternate)
# s_2 = str_2[::-1]
# print(s_2)


# 92. Please write a program which accepts a string from console and print the characters that have even indexes.
# Example: If the following string is given as input to the program:
# H1e2l3l4o5w6o7r8l9d
# Then, the output of the program should be:
# Helloworld

# METHOD 1 (Mine)
str_3 = input()
for i, c in enumerate(str_3):
    if i % 2 == 0:
        print(c, end="")

# METHOD 2 (Alternate)
# print(str_3[::2])


# 93. Please write a program which prints all permutations of [1,2,3]

# METHOD 1 (SEEN)
import itertools
print(list(itertools.permutations([1, 2, 3])))


# 94. Write a program to solve a classic ancient Chinese puzzle: We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have?

# METHOD 1 (Mine)
# head = 35
# leg = 94
# chicken_l = 2
# rabbit_l = 4

# 2L,  C_MAX == 23  (94)
# 4L == 12
def animals(head, leg, c_leg):
    rabbit = 0
    chicken = 0
    max_c = leg//c_leg  # Take animal with 2 legs as base.
    if max_c == head:
        chicken = max_c
        return f"Chicken = {chicken}, Rabbit= {rabbit}"
    else:
        while (chicken + rabbit != head):
            max_c = max_c - 2
            rabbit += 1
            chicken = max_c
    
        return f"Chicken = {chicken}, Rabbit= {rabbit}"

print(animals(35, 94, 2))



# METHOD 2 (Alternate)
# def solve(numheads,numlegs):
#     ns='No solutions!'
#     for i in range(numheads+1):
#         j=numheads-i
#         if 2*i+4*j==numlegs:
#             return i,j
#     return ns,ns

# numheads = 35
# numlegs = 94
# solutions=solve(numheads,numlegs)
# print(solutions)