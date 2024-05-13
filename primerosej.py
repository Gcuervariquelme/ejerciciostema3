def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    def sum_of_numbers(n):
        if n <= 0:
            return 0
        else:
            return n + sum_of_numbers(n-1)

    def product_of_numbers(a, b):
        return a * b

    def power(base, exponent):
        return base ** exponent