# DAY 7

# 20. Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.
# Suppose the following input is supplied to the program:
# 7
# Then, the output should be:
# 7

# METHOD 1 (Seen)
class MyGen():
    def by_seven(self, n):
        for i in range(0, int(n/7) + 1):
            yield i * 7

for i in MyGen().by_seven( int(input('Please enter a number... ')) ):
    print(i)

# METHOD 2 (Seen)
# class Divisible:
#     def by_seven(self,n):
#         for number in range(0, n + 1):
#             if number % 7 == 0:
#                 yield number

# divisible = Divisible()
# generator = divisible.by_seven(int(input("Please insert a number. --> ")))
# for number in generator:
#     print(number)




# 21. A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer. Example: If the following tuples are given as input to the program:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# Then, the output of the program should be:
# 2

# METHOD 1 (Mine)
from math import sqrt
x = 0
y = 0
while 1:
    inp = input().split(" ")
    if not inp[0]:
        break;
    if inp[0] == "UP":
        y += int(inp[1])
    if inp[0] == "DOWN":
        y -= int(inp[1])
    if inp[0] == "RIGHT":
        x += int(inp[1])
    if inp[0] == "LEFT":
        x -= int(inp[1])

distance = sqrt(x**2 + y**2)
print(round(distance))
