# DAY 21

# 85. By using list comprehension, please write a program to print the list after removing the 0th,4th,5th numbers in [12,24,35,70,88,120,155].

# METHOD 1 (Mine)
li = [12,24,35,70,88,120,155]
li_new = [v for i,v in enumerate(li) if i != 0 and i != 4 and i != 5]
print(li_new)

# METHOD 2 (Alternate)
# li = [12,24,35,70,88,120,155]
# li = [li[i] for i in range(len(li)) if i not in (0,4,5)]
# print(li)



# 86. By using list comprehension, please write a program to print the list after removing the value 24 in [12,24,35,24,88,120,155].

# METHOD 1 (Mine)
li = [12,24,35,24,88,120,155]
li_new_2 = [_ for _ in li if _ != 24]
print(li_new_2)

# METHOD 2 (Alternate)
# li = [12,24,35,24,88,120,155]
# li.remove(24)  # this will remove only the first occurrence of 24
# print(li)



# 87. With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155], write a program to make a list whose elements are intersection of the above given lists.

# METHOD 1 (Mine)
li_1 = [1,3,6,78,35,55,35]
li_2 = [12,24,35,24,88,120,155]

new_li = []
for i in li_1:
    for j in li_2:
        if i == j:
            new_li.append(i)

print(list(set(new_li)))

# METHOD 2 (Alternate)
list1 = [1,3,6,78,35,55]
list2 = [12,24,35,24,88,120,155]
set1= set(list1)
set2= set(list2)
intersection = set1 & set2
print(list(intersection))

# METHOD 3 (Alternate)
# list1 = [1,3,6,78,35,55]
# list2 = [12,24,35,24,88,120,155]
# set1= set(list1)
# set2= set(list2)
# intersection = set.intersection(set1,set2)
# print(list(intersection))



# 88. With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this list after removing all duplicate values with original order reserved.

# METHOD 1 (Mine)
li = [12,24,35,24,88,120,155,88,120,155]
set_o = list(set(li))
print(set_o)
set_o.reverse()
print(set_o)



# 89. Define a class Person and its two child classes: Male and Female. All classes have a method "getGender" which can print "Male" for Male class and "Female" for Female class.

# METHOD 1 (Mine)
class Person:
    def __init__(self):
        self.gender = "unknown"
    
    def getGender(self):
        print(self.gender)
    
class Male(Person):
    def __init__(self):
        self.gender = "Male"

class Female(Person):
    def __init__(self):
        self.gender = "Female"

sharon = Female()
doug = Male()
sharon.getGender()
doug.getGender()