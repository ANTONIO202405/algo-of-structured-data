# Fibonacci Sequence
# recursively
# memo = [None] * 100
# counter = 0
# def fib(n):
#     global counter
#     counter += 1
#     if memo[n] is not None:
#         return memo[n]
#     if n == 0 or n == 1:
#         return n
#     memo[n] = fib(n - 1) + fib(n - 2)
#     return memo[n]
# n = 35
# print("\nFib of", n, "=", fib(n))
# print("\nCounter:", counter)

#
# 9227465
# 29860703

# iteratively
counter = 0
def fib(n):
    fib_list = [0, 1]
    for index in range(2, n + 1):
        global counter
        counter += 1
        next_fib = fib_list[index - 1] + fib_list[index - 2]
        fib_list.append(next_fib)
    return fib_list[n]

n = 35
print("Fib of", n, "=", fib(n))
print("Counter:", counter)