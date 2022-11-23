def plusOne(digits):
    N = len(digits)
    for i in range(N-1, -1, -1):
        if digits[i] == 9:
            digits[i] = 0
        else:
            digits[i] += 1
            return digits
    return [1] + digits