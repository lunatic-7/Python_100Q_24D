# DAY 6

# 18. A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
# Following are the criteria for checking the password:
# At least 1 letter between [a-z]
# At least 1 number between [0-9]
# At least 1 letter between [A-Z]
# At least 1 character from [$#@]
# Minimum length of transaction password: 6
# Maximum length of transaction password: 12
# Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.
# Example
# If the following passwords are given as input to the program:
# ABd1234@1,a F1#,2w3E*,2We3345
# Then, the output of the program should be:
# ABd1234@1

# METHOD 1 (Mine) 
# import re

# password = re.compile(r"[A-Za-z0-9&%@$#]{6,12}")  # I created this re myself from regex101.com
# stri = input().split(",")
# li = []

# for _ in stri:
#     if password.fullmatch(_):
#        li.append(_) 

# print(",".join(li))

# METHOD 2 (Alternate)
def check(x):
    cnt = (6<=len(x) and len(x)<=12)
    for i in x:
        if i.isupper():
            cnt+=1
            break
    for i in x:
        if i.islower():
            cnt+=1
            break
    for i in x:
        if i.isnumeric():
            cnt+=1
            break
    for i in x:
        if i=='@' or i=='#'or i=='$':
            cnt+=1
            break
    return cnt == 5               # counting if total 5 all conditions are fulfilled then returns True

s = input().split(',')
lst = filter(check,s)             # Filter function pick the words from s, those returns True by check() function
print(",".join(lst))



# 19. You are required to write a program to sort the (name, age, score) tuples by ascending order where name is string, age and score are numbers. The tuples are input by console. The sort criteria is:
# 1: Sort based on name
# 2: Then sort based on age
# 3: Then sort by score
# The priority is that name > age > score.
# If the following tuples are given as input to the program:
# Tom,19,80
# John,20,90
# Jony,17,91
# Jony,17,93
# Json,21,85
# Then, the output of the program should be:
# [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]

# METHOD 1 (Mine)
col = []
while 1:
    srt = input().split(",")
    if not srt[0]:
        break;
    col.append(tuple(srt))

temp = sorted(col)
print(temp)

