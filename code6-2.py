#2分探索を一般化
a=list(map(int,input().split()))
#keyの場所を特定
#現段階でのindexよりもkeyが小さければtrueを返す
def P(key,index): #key:探したい文字
    if a[index]>=key:
        return True
    else:
        return False
def binary_search(key):
    left=-1
    right=int(len(a))
    while right-left>1:
        mid=left+(right-left)//2
        if P(key,mid):
            right=mid
        else:
            left=mid
    return right

print(binary_search(10))
print(binary_search(100))