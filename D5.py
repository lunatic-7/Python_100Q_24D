# DAY 5

# 16. Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers. >Suppose the following input is supplied to the program:
# 1,2,3,4,5,6,7,8,9
# Then, the output should be:
# 1,9,25,49,81

# METHOD 1 (Mine)
lis = []
li = input().split(",")
for _ in li:
    if (int(_) % 2 != 0):
        lis.append(str(int(_)**2))

print(",".join(lis))

# METHOD 2 (Alternate)
# lst = [str(int(i)**2) for i in input().split(',') if int(i) % 2]
# print(",".join(lst))


# 17. Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
# D 100
# W 200
# D means deposit while W means withdrawal.
# Suppose the following input is supplied to the program:
# D 300
# D 300
# W 200
# D 100
# Then, the output should be:
# 500

# METHOD 1 (Mine)
amount = 0
while 1:
    t_type = input().split()
    if not t_type:  # break if the string is empty
        break
    if t_type[0] == "D":
        amount += int(t_type[1])
    elif t_type[0] == "W":
        amount -= int(t_type[1])
print(amount)

# METHOD 2 (Alternate)
# account = 0
# while True:
#     action = input("Deposit/Whitdrow/Balance/Quit? D/W/B/Q: ").lower()
#     if action == "d":
#         deposit = input("How much would you like to deposit? ")
#         account = account + int(deposit)
#     elif action == "w":
#         withdrow = input("How much would you like to withdrow? ")
#         account = account - int(withdrow)
#     elif action == "b":
#         print(account)
#     else:
#         quit()