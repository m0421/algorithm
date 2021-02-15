#2分探索
N=int(input()) #配列の長さ
a=list(map(int,input().split())) #配列
def binary_search(k): #探す文字を入力
    left=0
    right=N-1 
    while left<=right:
        mid=(left+right)//2 #現段階での中央値     
        if a[mid]==k:
            return mid
        if a[mid]<k:
            right=mid-1
        if a[mid]<k:
            left=mid+1
    return -1
print(binary_search(10))
print(binary_search(100))
