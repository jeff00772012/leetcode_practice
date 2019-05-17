def twoSum( nums: [int], target: int) -> [int]:
        dff_all={}
        for xx in range(len(nums)):
          dff=target-nums[xx]
          if dff in dff_all:
             return [dff_all[dff],xx]
          dff_all[nums[xx]]=xx

        
a=twoSum([-3,4,3,90],0)        
print(a)
