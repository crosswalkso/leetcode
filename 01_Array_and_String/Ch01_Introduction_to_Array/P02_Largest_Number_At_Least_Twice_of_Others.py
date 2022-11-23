def dominantIndex(nums):
    MAX_NUM = max(nums)
    for i, v in enumerate(nums):
        if v!= MAX_NUM and 2*v > MAX_NUM:
            return -1
        if v == MAX_NUM:
            ans = i

    return ans