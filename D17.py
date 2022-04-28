# DAY 17

# 65. Please write assert statements to verify that every number in the list [2,4,6,8] is even.

# METHOD 1 (Mine)
li = [2,4,6,8]

for _ in li:
    assert _ % 2 == 0, f"{_} is not an even number!"



# 66. Please write a program which accepts basic mathematic expression from console and print the evaluation result.
# Example: If the following n is given as input to the program:
# 35 + 3
# Then, the output of the program should be:
# 38

# METHOD 1 (Mine)
ev = input()
print(eval(ev))



# 67. Please write a binary search function which searches an item in a sorted list. The function should return the index of element to be searched in the list.

# METHOD 1 (SEEN)
def binary_search_ascending(array, target):
    lower = 0
    upper = len(array)
    print(f"Length of array: {upper}")
    while lower < upper:
        x = (lower + upper) // 2
        print(f"Middle value: {x}")
        value = array[x]
        print(value)
        if target == value:
            return x
        elif target < value:
            upper = x
        elif target > value:
            lower = x


array = [12,34,2,45565,3,45,26,77,38,22,44,0,11,93,332,33]
sorted_array = sorted(array)
print(sorted_array)
print(f"The value 11 is at position: {binary_search_ascending(sorted_array, 11)}")



# 68. Please generate a random float where the value is between 10 and 100 using Python module.

# METHOD 1 (Mine)
import random 
print(10 + (random.random()* 90))

# METHOD 2 (Alternate)
# rand_num = random.uniform(10,100)
# print(rand_num)



# 69. Please generate a random float where the value is between 5 and 95 using Python module.

# METHOD 1 (Mine)
rand_num = random.uniform(5,95)
print(rand_num)