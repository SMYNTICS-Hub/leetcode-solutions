#Two Sum - Bruteforce Approach

def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if(nums[i]+ nums[j]) == target:
                return[i,j]

nums = [2,11,7,15]
target = 9
print(two_sum(nums,target))