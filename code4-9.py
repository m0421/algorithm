#部分和問題を再帰関数で解く
#配列aの中からi個選んで和をwにすることができるかの関数
#計算量はオーダーの2**n

def func(i,w,a):
    if(i==0):
        if(w==0):
            return True
        else:
            return False
    #i-1で再帰を使う
    #a[i-1]を選ばない場合
    if func(i-1,w,a):
        return True
    #a[i-1]を選ぶ場合
    if func(i-1,w-a[i-1],a):
        return True
    #どちらも無理な場合
    return False

N, W = map(int, input().split())
a = list(map(int, input().split()))
if func(N, W, a):
    print("Yes")
else:
    print("No")