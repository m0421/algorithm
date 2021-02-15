#整数bitの表す部分集合にi番目の要素が含まるかどうかを判定
#bit全探索の下準備
#入力
n,k= map(int, input().split())
a = list(map(int, input().split()))
flag = 0

#全探索
for bit in range(1<<n): #2**nを回すことと同意
    sum=0 #要素の合計を格納する
    for i in range(n):
        if bit & (1 << i): #i番目の要素a[i]が部分集合に含まれるかどうか
            sum+= a[i]
        if sum==k:
            flag=1
if flag==1:
    print("Yes")
else:
    print("No")
