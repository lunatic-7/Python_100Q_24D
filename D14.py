# DAY 14

# 51. Write a function to compute 5/0 and use try/except to catch the exceptions.

# METHOD 1 (Mine)
def throw():
    return 5/0

try:
    print(throw())
except ZeroDivisionError:
    print("Division by Zero!")
except:
    print("Unknown Error!")



# 52. Define a custom exception class which takes a string message as attribute.

# METHOD 1 (Mine)
class CustomException(Exception):
    """Exception raised for custom purpose

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message):
        self.message = message


num = int(input())

try:
    if num < 10:
        raise CustomException("Input is less than 10")
    elif num > 10:
        raise CustomException("Input is grater than 10")
except CustomException as ce:
    print("The error raised: " + ce.message)



# 53. Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the user name of a given email address. Both user names and company names are composed of letters only.
# Example: If the following email address is given as input to the program:
# john@google.com
# Then, the output of the program should be:
# john

# METHOD 1 (Mine)
inp = input()
temp = inp.split("@")
print(temp[0])

# METHOD 2 (Alternate)
import re

email = "john@google.com elise@python.com"
pattern = "(\w+)@\w+.com"
ans = re.findall(pattern,email)
print(ans)
