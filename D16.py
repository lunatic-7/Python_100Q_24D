# DAY 16

# 60. Write a program to compute:
# f(n)=f(n-1)+100 when n>0
# and f(0)=0
# with a given n input by console (n>0).
# Example: If the following n is given as input to the program:
# 5
# Then, the output of the program should be:
# 500

# METHOD 1 (Mine)
n = int(input())

def rec(n):
    if n == 0:
        return 0
    return rec(n - 1) + 100

print(rec(n))

# METHOD 2 
# num = 0
# while n != 0:
#     if n == 0:
#         break
#     num += 100
#     n = n - 1

# print(num)



# 61. The Fibonacci Sequence is computed based on the following formula:
# f(n)=0 if n=0
# f(n)=1 if n=1
# f(n)=f(n-1)+f(n-2) if n>1
# Please write a program to compute the value of f(n) with a given n input by console.
# Example: If the following n is given as input to the program:
# 7
# Then, the output of the program should be:
# 13

# METHOD 1 (Mine)
m = int(input())

def fib(m):
    if m == 0:
        return 0
    if m == 1:
        return 1
    return fib(m-1) + fib(m-2)

print(fib(m))

# METHOD 2 (Alternate)
# n = int(input())
# f = lambda x: 0 if x == 0 else 1 if x == 1 else f(x-1)+f(x-2)
# print(','.join([str(f(x)) for x in range(0, n+1)]))



# 62. The Fibonacci Sequence is computed based on the following formula:
# f(n)=0 if n=0
# f(n)=1 if n=1
# f(n)=f(n-1)+f(n-2) if n>1
# Please write a program to compute the value of f(n) with a given n input by console.
# Example: If the following n is given as input to the program:
# 7
# Then, the output of the program should be:
# 0,1,1,2,3,5,8,13

# METHOD 1 (Mine)
n = int(input())
f = lambda n: n if n < 2 else f(n-1) + f(n-2)
print(",".join([str(f(_)) for _ in range(0, n + 1)]))

# METHOD 2 (Alternate)
# def question_62(n):
#     if n == 0:
#         return [0]
#     if n == 1:
#         return [0, 1]
#     sequence = [0, 1]
#     a, b = 0, 1
#     for x in range(2, n+1):
#         c = a + b
#         sequence.append(c)
#         a = b
#         b = c
#     return sequence

# print(question_62(n))



# 63. Please write a program using generator to print the even numbers between 0 and n in comma separated form while n is input by console.
# Example: If the following n is given as input to the program:
# 10
# Then, the output of the program should be:
# 0,2,4,6,8,10

# METHOD 1 (Mine)
n = int(input())

for i in range(0, n+1, 2):
  if i < n - 1:
    print(i, end = ',' )
  else:
    print(i)



# 64. Please write a program using generator to print the numbers which can be divisible by 5 and 7 between 0 and n in comma separated form while n is input by console.
# Example: If the following n is given as input to the program:
# 100
# Then, the output of the program should be:
# 0,35,70

# METHOD 1 (SEEN)
def generate(n):
    for i in range(n+1):
        if i % 35 == 0:    # 5*7 = 35, if a number is divisible by a & b then it is also divisible by a*b
            yield i

n = int(input())
resp = [str(i) for i in generate(n)]
print(",".join(resp))
