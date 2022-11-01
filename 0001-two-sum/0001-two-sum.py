class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #approach 1
        
        my_dict = {}
        
        for i, value in enumerate(nums):
            sum = target-nums[i]
            if sum in my_dict:
                return [my_dict[sum],i]
            my_dict[value] = i

# i = 0, d = {3:0}
# i = 1, 6-nums[1]:(6-2)=4, d = {3:0,2:1}
# i = 2, 6-nums[2]:(6-4)=2 : return [d[2],2]