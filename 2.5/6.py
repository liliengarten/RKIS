def reverse_numbers(*nums):
    nums = list(nums)

    for i in range(len(nums)):
        nums[i] = nums[i] * -1

    return nums