
def fib(n):
    if n==0:
        return 0
    if n==1:
        return 1
    if dp[n]!=-1:
        return dp[n]
    else:
        dp[n]=fib(n-1)+fib(n-2)
        return dp[n]
n=7       
dp=[-1]*(n+1)

print(fib(n))
    
    