def sum_numbers_until_zero(nums: list):
    total = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            break
        else:
            total += nums[i]
    return total

print(sum_numbers_until_zero([1,4,3,0,5]))