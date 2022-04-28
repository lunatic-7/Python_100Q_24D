# DAY 12

# 44. Write a program which can map() to make a list whose elements are square of numbers between 1 and 20 (both included).

# METHOD 1 (Mine)
no = map(lambda x: x**2,range(1,21))
print(list(no))



# 45. Define a class named Indian which has a static method called printNationality.

# METHOD 1 (Mine)
class Indian():
    @staticmethod
    def printNationality():
        print("I am Indian.")
    
anIndian = Indian()
anIndian.printNationality()   # this will not run if @staticmethod does not decorates the function.
                              # Because the class has no instance.

Indian.printNationality()     # this will run even though the @staticmethod
                              # does not decorate printNationality()



# 46. Define a class named American and its subclass NewYorker.

# METHOD 1 (Mine)
class American():
    pass

class NewYorker(American):
    pass

american = American()
newyorker = NewYorker()

print(american)
print(newyorker)