# DAY 10

# 31. Define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys.

# METHOD 1 (Mine)
d= {}
def sq():
    for _ in range(1,21):
        d[_] = _ ** 2  # To append to an empty dictionary.
sq()
print(d)

# METHOD 2 (Alternate)
# def printDict():
#     dict={i:i**2 for i in range(1,21)}   # Using comprehension method and
#     print(dict)

# printDict()



# 32. Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys. The function should just print the keys only.

# METHOD 1 (Mine)
def sq2():
    dict={_:_**2 for _ in range(1,21)}
    print(dict.keys())

sq2()



# 33. Define a function which can generate and print a list where the values are square of numbers between 1 and 20 (both included).

# METHOD 1 (Mine)
def sq3():
    li = [_**2 for _ in range(1,21)]
    print(li)

sq3()



# 34. Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print the first 5 elements in the list.

# METHOD 1 (Mine)
def sq4():
    li = [_**2 for _ in range(1,21)]
    print(li[:5])

sq4()

# METHOD 2 (Alternate)
# func = lambda :print([i**2 for i in range(1,21)][:5])
# func()



# 35. Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print the last 5 elements in the list.

# METHOD 1 (Mine)
func2 = lambda : print([_**2 for _ in range(1,21)][-5:])
func2()



# 36. Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print all values except the first 5 elements in the list.

# METHOD 1 (Mine)
func3 = lambda : print([_**2 for _ in range(1,21)][5:])
func3()



# 37. Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20 (both included).

# METHOD 1 (Mine)
func4 = lambda : print(tuple([_ ** 2 for _ in range(1,21)]))
func4()