# Fix the problems with each of these classes (1-3).

# 1
class MyClass():
    def __init__(self):
        a = 10
        b = 20
        self.x = a + b
my_instance = MyClass()
my_instance.x

# 2
class MyClass():
    def __init__(self):
        a = 10
        b = 20
        self.x = a + b
my_instance = MyClass()
my_instance.x

# 3
class MyClass():
    def __init__(self,a, b):
        self.x = a + b
my_instance = MyClass(10, 20)
my_instance.x

# 4 A Fibonacci sequence is a list of values where each is the sum of the 
# previous two, e.g. [0, 1, 1, 2, 3].
#      - First write a function that takes in a list of any two values, then
#        calculates the rest of the sequence starting from that point.  It
#        should have two arguments:  the starting list and the number of 
#        additional Fibonacci sequence elements to calculate.
#      - Second, turn this into a class that takes the same list at start,
#        but has a method that takes only the number of additional Fibonacci 
#        sequence elements as an argument and then calculates the sequence.
#  Note that technically the Fibonacci sequence starts at 0, but for our
#  coding practice we can calculate it from any two starting values.



class FibonacciSequence():
    def __init__(self):
        self.fib = [0,1]
    def fibonacci(self,n):
        if n < len(self.fib):
            return self.fib[n]
        else:
            fib_number = self(n-1) + self(n-2)
            self.fib.append(fib_number)
            return self.fib[n]

fib_instance = FibonacciSequence()
fib_instance.fibonacci(4)