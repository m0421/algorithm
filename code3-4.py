#ペア和の最小値を求める
#全探索
N,K=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
ans=10000
for i in range(N):
    for j in range(N):
        if a[i]+b[i]>=K:
            ans=min(ans,a[i]+b[i])
print(ans)