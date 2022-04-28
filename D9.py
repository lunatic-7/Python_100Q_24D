# DAY 9

# 26. Define a function which can compute the sum of two numbers.

# METHOD 1 (Mine)
def sum_2(num1, num2):
    total = num1 + num2
    return total
print(sum_2(2,3))

# METHOD 2 (Alternate)
# sum = lambda n1,n2 : n1 + n2      # here lambda is use to define little function as sum
# print(sum(1,2))



# 27. Define a function that can convert a integer into a string and print it in console.

# METHOD 1 (Mine)
convert = lambda integer : str(integer)
print(convert(int(input())))



# 28. Define a function that can receive two integer numbers in string form and compute their sum and then print it in console.

# METHOD 1 (Mine)
sum_3 = lambda num1,num2 : int(num1) + int(num2)
print(sum_3("1","4"))



# 29. Define a function that can accept two strings as input and concatenate them and then print it in console.

# METHOD 1 (Mine)
conc = lambda str1,str2 : f"{str1}{str2}"
print(conc("Hello I am ", "John Cena."))



# 30. Define a function that can accept two strings as input and print the string with maximum length in console. If two strings have the same length, then the function should print all strings line by line.

# METHOD 1 (Mine)
def max_len(str1, str2):
    if(len(str1) > len(str2)):
        print(str1)
    elif(len(str1) == len(str2)):
        print(str1)
        print(str2)
    else:
        print(str2)

print("Input bta bro!")
str1 = input()
str2 = input()
max_len(str1,str2)
