def findDiagonalOrder(mat):
    m = len(mat)
    n = len(mat[0])
    X = m+n-1

    ans = []
    intermediate = []
    for x in range(X):
        intermediate.clear()
        r = 0 if x<n else x-n+1
        c = x if x<n else n-1

        while r<m and c>-1:
            intermediate.append(mat[r][c])
            r+=1
            c-=1
        
        if x % 2 == 0:
            ans += intermediate[::-1]
        else:
            ans += intermediate
    return ans


def review_20220926(mat):
    rows = len(mat)
    cols = len(mat[0])
    L = rows + cols - 1

    ans = []
    intermediate = []
    for l in range(L):
        r = 0 if l < cols else l-cols+1
        c = l if l < cols else cols-1
        intermediate.clear()
        while r<rows and c>-1:
            intermediate.append(mat[r][c])
            r+=1
            c-=1
            if l%2 == 0:
                ans += intermediate[::-1]
            else:
                ans += intermediate
    return ans