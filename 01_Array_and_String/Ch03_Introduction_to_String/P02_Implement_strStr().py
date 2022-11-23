def strStr(haystack, needle):
    h = len(haystack)
    n = len(needle)
    idx = -1
    # haystack 각 자리에 대해 모든 needle을 검사
    for i in range(h-n+1):
        # needle 좌우가 맞지 않을 때
        if haystack[i] != needle[0] or haystack[i+n-1] != needle[-1]:
            continue
        # needle 좌우가 맞으면
        else: 
            idx = i
            # 예외처리
            if n<=2:
                return idx
        for j in range(1, n-1):
            # haystack과 needle이 다르면
            if haystack[i+j]!=needle[j]:
                idx = -1
                break # 검사 중단
            if j == n-2 and haystack[i+j]==needle[j]:
                return idx
    return idx