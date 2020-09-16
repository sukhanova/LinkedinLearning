#Recursion - defining something in terms of itself to achieve your objective

#Recursive Function - a function that calls itself in its body

# A recursive function solves a problem by dividing problem into smaller subproblems, and calling the function itself to solve each problem


#Factorial
# 1! = 1
# 2! = 2 * 1 = 2
# 3! = 3 * 2 * 1 = 6
# 4! = 4 * 3 * 2 * 1 = 24
# 5! = 5 * 4 * 3 * 2 * 1 = 120
# 6! = 6 * 5 * 4 * 3 * 2 * 1 = 720


def factorial(n):
    """Return the factorial of positive integer n.
    """
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
        


n = input("Please type in number: ")
n = int(n)
def factorial(n):
    """Return the factorial of positive integer n.
    """
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)


print(factorial(n))


