# DAY 11

# 38. With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values in one line and the last half values in one line.

# METHOD 1 (Mine)
tu = (1,2,3,4,5,6,7,8,9,10)
print(tu[:5])
print(tu[5:])



# 39. Write a program to generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).

# METHOD 1 (Mine)
tu = (1,2,3,4,5,6,7,8,9,10)
li = []
for _ in tu:
    if _ % 2 == 0:
        li.append(_)

print(tuple(li))

# METHOD 2 (Alternate)
# tpl = (1,2,3,4,5,6,7,8,9,10)
# tpl1 = tuple(filter(lambda x : x%2==0,tpl))  # Lambda function returns True if found even element.
#                                              # Filter removes data for which function returns False
# print(tpl1)



# 40. Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes", otherwise print "No".

# METHOD 1 (Mine)
inp = input()

if (inp == "yes" or inp == "YES" or inp == "Yes"):
    print("Yes")
else:
    print("No")

# METHOD 2 (Alternate)
# print("Yes") if (inp == "yes" or inp == "YES" or inp == "Yes") else print("No")



# 41. Write a program which can map() to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10].

# METHOD 1 (Mine)
li = [1,2,3,4,5,6,7,8,9,10]
squaredNumbers = map(lambda x : x**2, li) # map iterates the 2nd parameter in first and returns map type object data
print(list(squaredNumbers))  # converting the object into list



# 42. Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10].

# METHOD 1 (Mine)
def even(x):
    return x%2==0

def squer(x):
    return x*x

li = [1,2,3,4,5,6,7,8,9,10]
li = map(squer,filter(even,li))   # first filters number by even number and the apply map() on the resultant elements
print(list(li))



# 43. Write a program which can filter() to make a list whose elements are even number between 1 and 20 (both included).

# METHOD 1 (Mine)
lis = []
for _ in range(1,21):
    lis.append(_)

li = filter(lambda x: x % 2 == 0, lis)
print(list(li))

# METHOD 2 (Alternate)
# evenNumbers = filter(lambda x: x%2==0, range(1,21))
# print(list(evenNumbers))