#メモ化
#動的計画法
def fib2(n):
    memo=[0]*(n+1)
    def fib3(n):
        if n<=1:
            return n
        if memo[n]!=0:
            return memo[n]
        memo[n]=fib3(n-1)+fib3(n-2)
        return memo[n]
    return fib3(n)
print(fib2(10))
