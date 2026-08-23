def fibonacci(n, memo):

    if n == 1:
        return 1

    if n ==0:
        return 0

    if n in memo.values():
        return memo[n]
    
    f = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    memo[n] = f
    return f

memo = {}

n = int(input("Enter the digit to calculate fibonacci series"))
print(fibonacci(n, memo))