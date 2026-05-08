from merge_sort import merge_sort
from quick_sort import quick_sort

nums = [17, -4, 29, 0, 13, -22, 8, 45, -9, 31,
        6, -15, 27, 3, -1, 50, -33, 12, 19, -7,
        41, 2, -18, 25, 9, -11, 36, 14, -2, 48]


def s3sum(nums):
    nums = quick_sort(nums)
    # return nums

    for i in range(len(nums)):
        fnum = nums[i]

        left = i + 1
        right = len(nums) - 1

        while left < right:
            total = fnum + nums[left] + nums[right]
            if total < 0 :
                left += 1
            elif total > 0:
                right -= 1
            else:
                return [fnum,nums[left],nums[right]]
                break



print(s3sum(nums))