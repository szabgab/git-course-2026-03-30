print("Hello World")

def fib(n):
    if n == 1:
        return 0
    if n == 2:
        return 0
    fibs = [0, 1]
    for _ in range(n-2):
        fibs.append(fibx[-1] + fibx[-2])
