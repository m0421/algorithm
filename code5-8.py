def levenshtein(s1,s2):
    n,m=len(s1),len(s2)

    #dpテーブルを定義
    dp=[[0]*(m+1) for i in range(n+1)]

    #dp初期設定
    for i in range(n+1):
        dp[i][0]=i
    for j in range(m+1):
        dp[0][j]=j

    for i in range(1,n+1):
        for j in range(1,m+1):
            if s1[i-1] == s2[j-1]:
                cost=0
            else:
                cost=1
            dp[i][j] = min(dp[i - 1][j] + 1,         # insertion
                           dp[i][j - 1] + 1,         # deletion
                           dp[i - 1][j - 1] + cost)  # replacement
    return dp[n][m]
S,T=map(str,input().split())
print(levenshtein(S,T))

