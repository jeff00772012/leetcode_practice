def searchInsert(nums: [int], target: int) -> int:
    nums[:]=[x-target for x in nums]
    if 0 in nums:
        return nums.index(0)
    else:
        print(nums)
        neg = [nums.index(x) for x in nums if x < 0]
        if len(neg)==0:
            return 0
        else:
            
            return neg[len(neg)-1]+1

print(searchInsert([1,3,5,6],0))
