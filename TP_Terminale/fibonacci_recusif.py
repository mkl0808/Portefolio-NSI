def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

def fibonacci_list(n, l):
    if n < 2:
        l[n] = n
        return n
    l[n] = fibonacci_list(n-1, l) + fibonacci_list(n-2, l)
    return l[n]

n = 40
l = [0] * (n+1)
fibonacci_list(n, l)
print(l)