import random

nums = [42, -7, 13, 0, 88, -23, 5, 19, -11, 64, 2, -35, 77, 9, -4]

def quick_sort(nums):
    if len(nums) <= 1:
        return nums 

    pivot = nums[random.randint(0,len(nums) - 1)]  

    
    small =[]
    large = []
    equal =[]
    for i in range(len(nums)):
        if nums[i] < pivot:
            small.append(nums[i])
        elif nums[i] > pivot:
            large.append(nums[i])
        else:
            equal.append(nums[i])

    return quick_sort(small) + equal + quick_sort(large)




print(quick_sort(nums))