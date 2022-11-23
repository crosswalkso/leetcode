def longestCommonPrefix(strs):
    L = len(strs)
    prefix = strs[0]
    n = len(prefix)
    ans = ""
    for i in range(n):
        for j in range(1, L):
            m = len(strs[j])
            # 끝에 도달했으면 결과 리턴
            if m <= i:
                return ans
            # 더이상 같지 않으면 결과 리턴
            if prefix[i] != strs[j][i]:
                return ans
        ans += prefix[i]
    return ans