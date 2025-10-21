def sum_numbers_until_zero(nums: list):

    """
    Calculate the sum of numbers in a list until a zero is encountered.

    Parameters:
    nums (list): A list of integers.

    Returns:
    int: The sum of integers in the list up to (but not including) the first zero.
    """

    total = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            break
        else:
            total += nums[i]
    return total

print(sum_numbers_until_zero([1, 2, 3, 0]))

