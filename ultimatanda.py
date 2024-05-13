def euclidean_algorithm(a, b):
    while b != 0:
        remainder = a % b
        a = b
        b = remainder
    return a

def gcd(a, b):
    return euclidean_algorithm(a, b)

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def sum_of_digits(n):
    total = 0
    while n != 0:
        total += n % 10
        n //= 10
    return total