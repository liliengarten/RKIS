def homework(*nums):
    pos_summ = 0
    range_mult = 1

    for num in nums:
        if num > 0:
            pos_summ += num

    for i in range(nums.index(min(nums)), nums.index(max(nums)) + 1):
        range_mult *= nums[i]

    return pos_summ, range_mult