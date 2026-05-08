import random

nums = [42, -7, 13, 0, 88, -23, 5, 19, -11, 64, 2, -35, 77, 9, -4]

# pi vot = nums[random.randi nt(0, len(nums) - 1)]
# pri nt(pi vot)

def merged_sort(nums):
    mid = len(nums)//2
    
    if len(nums) == 1:
        return nums

    left = nums[:mid]
    right = nums[mid:]

    l = merged_sort(left)
    r = merged_sort(right)
    result = []
    i,j = 0,0
    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            result.append(l[i])
            i += 1
        else:
            result.append(r[j])
            j += 1 
    
    while i < len(l) :
        result.append(l[i])
        i +=1

    while j < len(r):
        result.append(r[j])
        j +=1 
    
    return result

print(merged_sort(nums))