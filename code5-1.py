#Flog問題
#DP 動的計画法
N=int(input())
h=list(map(int,input().split()))
dp=[]
dp.append(0)
dp.append(abs(h[0]-h[1]))
for i in range(2,N):
    x=min(dp[i-1]+abs(h[i]-h[i-1]),dp[i-2]+abs(h[i]-h[i-2]))
    dp.append(x)
print(dp[N-1])