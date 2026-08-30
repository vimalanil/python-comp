# Fibonacci sequence using dynamic programming
def fib(n):

    if n <= 1:
        return n

    return fib(n - 1) + fib(n - 2)
n = 10
fib(n)

# Fibonacci sequence using dynamic programming with memoization
def fib_memo(n, memo={}):
    if n in memo:
        return memo[n]

    if n <= 1:
        return n

    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]

# Fibonacci sequence using dynamic programming with tabulation
def fib_tab(n):
    if n <= 1:
        return n

    dp = [0] * (n + 1)
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]    