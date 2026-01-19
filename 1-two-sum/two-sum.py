class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        def check(x,y):
            if x>= len(nums):
                return None
            for i in range(y,len(nums)):
                if nums[x]+nums[i]==target:
                    return [x,i]
            return check(x+1,y+1)
        return check(x=0,y=1)
            
        