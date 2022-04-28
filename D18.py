# DAY 18

# 70. Please write a program to output a random even number between 0 and 10 inclusive using random module and list comprehension.

# METHOD 1 (SEEN)
import random
r_even = [_ for _ in range(0,11,2)]
print(random.choice(r_even))



# 71. Please write a program to output a random number, which is divisible by 5 and 7, between 10 and 150 inclusive using random module and list comprehension.

# METHOD 1 (Mine)
divisible = [_ for _ in range(10,151) if _ % 35 == 0]
print(divisible)
print(random.choice(divisible))



# 72. Please write a program to generate a list with 5 random numbers between 100 and 200 inclusive.

# METHOD 1 (Seen)
print(random.sample(range(100,201), 5))



# 73. Please write a program to randomly generate a list with 5 even numbers between 100 and 200 inclusive.

# METHOD 1 (Mine)
print(random.sample(range(100,201,2), 5))



# 74. Please write a program to randomly generate a list with 5 numbers, which are divisible by 5 and 7 , between 1 and 1000 inclusive.

# METHOD 1 (Mine)
lst = [_ for _ in range(1,1001) if _ % 35 == 0]
print(random.sample(lst, 5))
