# DAY 4

# 14. Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
# Suppose the following input is supplied to the program:
# Hello world!
# Then, the output should be:
# UPPER CASE 1
# LOWER CASE 9

# METHOD 1 (Mine)
string = input()

upper = 0
lower = 0
for _ in string:
    if _.isupper():
        upper += 1
    elif _.islower():
        lower += 1

print(f"UPPER CASE {upper}")
print(f"LOWER CASE {lower}")



# 15. Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
# Suppose the following input is supplied to the program:
# 9
# Then, the output should be:
# 11106

# METHOD 1 (Mine)
x = int(input())
num = x+(x*10+x)+(x*100+x*10+x)+(x*1000+x*100+x*10+x)
print(num)

# METHOD 2 (Alternate)
# a = input()
# total,tmp = 0,str()        # initialing an integer and empty string

# for i in range(4):
#     tmp+=a               # concatenating 'a' to 'tmp'
#     total+=int(tmp)      # converting string type to integer type

# print(total)

# # METHOD 3 (Alternate)
# a = input()
# total = int(a) + int(2*a) + int(3*a) + int(4*a)  # N*a=Na, for example  a="23", 2*a="2323",3*a="232323"
# print(total)