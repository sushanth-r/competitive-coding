def getNthFib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    fib_1 = result = 0
    fib_2 = 1
    index = 3
    while index <= n:
        result = fib_1 + fib_2
        fib_1 = fib_2
        fib_2 = result
        index += 1
    return result


class NthFibonacci:
    n = int(input())
    print(getNthFib(n))
