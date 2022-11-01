class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #approach 1
        n = len(nums)
        
        seen = {}
        for i, value in enumerate(nums): #1
            remaining = target - nums[i] #2
            if remaining in seen: #3
                return [i, seen[remaining]]  #4
            else:
                seen[value] = i  #5
        
#         my_dict = {}
        
#         for i in range(n):
#             sum = target-nums[i]
#             if sum in my_dict:
#                 return [my_dict[sum],i]
#             my_dict[nums[i]] = i

# i = 0, d = {3:0}
# i = 1, 6-nums[1]:(6-2)=4, d = {3:0,2:1}
# i = 2, 6-nums[2]:(6-4)=2 : return [d[2],2]