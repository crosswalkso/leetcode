nums = [1,7,3,6,5,6]
def pivotIndex(nums):
    left_sum = 0
    S = sum(nums)
    for i in range(len(nums)):
        right_sum = S - left_sum - nums[i]
        if right_sum == left_sum:
            return i
        left_sum += nums[i]
    return -1