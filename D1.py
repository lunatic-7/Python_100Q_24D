# DAY 1

# 1. Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated
# sequence on a single line.

# Method 1 (Mine)
print("\nQ1")
li = []
def mult(r1, r2):
    for _ in range(r1, r2):
        if (_ % 7 == 0) and (_ % 5 != 0):
            li.append(_)

mult(2000,3201)   # To include 3200 we need to give range 1+
print(li)
        
# Method 2 (Alternate) Using generators and list comprehension
# print(*(i for i in range(2000, 3201) if i%7 == 0 and i%5 != 0), sep=",")



# 2. Write a program which can compute the factorial of a given numbers.The results should be printed in a 
# comma-separated sequence on a single line.Suppose the following input is supplied to the program: 8 
# Then, the output should be:40320 

print("\nQ2")

# Method 1 (Mine)
num = int(input())
def fact(num) :
    new_num = 1
    for _ in range(1, num) :
        new_num = new_num * (_ + 1)
    print(new_num)

fact(num)

# Method 2 (Alternate) Using Lambda Function
# n = int(input())
# def shortFact(x): 
#     return 1 if x <= 1 else x*shortFact(x-1)
# print(shortFact(n))



# 3. With a given integral number n, write a program to generate a dictionary that contains (i, i x i) 
# such that is an integral number between 1 and n (both included). and then the program should print 
# the dictionary.Suppose the following input is supplied to the program: 8
# Then, the output should be:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

print("\nQ3")

# Method 1 (Mine)
num_2 = int(input())
dic = {}
def di(num_2):
    for _ in range(1, num_2 + 1):
        dic[_] = _ * _
    print(dic)

di(num_2)

# Method 2 (Alternate) Using dictionary comprehension
# n = int(input())
# ans={i : i*i for i in range(1,n+1)}
# print(ans)