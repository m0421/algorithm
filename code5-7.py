#ナップサック問題
#DP入門
N,W=map(int,input().split())
w=[0]*(N+1)
v=[0]*(N+1)

for i in range(1,N+1):
    w[i],v[i]=map(int,input().split())

dp=[[0]*(W+1) for i in range(N+1)]

for i in range(1,N+1):
    for j in range(1,W+1):
        if j>=w[i]:
            #そのまま更新した方がいいのかそれとも価値を多足して更新するのか
            dp[i][j]=max(dp[i-1][j-w[i]]+v[i],dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]

for i in range(N+1):
    print(dp[i])
print(dp[N][W])