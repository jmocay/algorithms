"""
    1, 1, 2, 3, 5 ... (n-1)+(n-2)
"""
def fibonacci(n):
    memo = {
        0: 0,
        1: 1
    }
    return fib_helper(n, memo)

def fib_helper(n, memo):
    if n in memo:
        return memo[n]
    fib = fib_helper(n-1, memo) + fib_helper(n-2, memo)
    memo[n] = fib
    return fib

if __name__ == '__main__':
    n = 10
    fib = [fibonacci(i) for i in range(n+1)]
    print(fib)
