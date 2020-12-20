from time import monotonic


def timer(func, *args, **kwargs):
    pass


def fibonacci(n):
    if n <= 0:
        print("Incorrect input")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


timer(fibonacci, 32)

