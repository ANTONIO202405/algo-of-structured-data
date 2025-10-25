
'''
def func_three():
    print("Three")

def func_two():
    func_three()
    print("Two")

def func_one():
    func_two()
    print("one")

func_one()
'''


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)
print(factorial(5))
