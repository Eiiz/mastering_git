import random

# nums = [17, -4, 29, 0, 13, -22, 8, 45, -9, 31,
#         6, -15, 27, 3, -1, 50, -33, 12, 19, -7,
#         41, 2, -18, 25, 9, -11, 36, 14, -2, 48] # them conflict

# # pi vot = nums[random.randint(0, len(nums) - 1)]
# # pri nt(pi vot)

def merge_sort(nums):
    mid = len(nums)//2
    
    if len(nums) == 1:
        return nums

    left = nums[:mid]
    right = nums[mid:]

    l = merge_sort(left)
    r = merge_sort(right)
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

# print(merge_sort(nums))