class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        #1st approach
#         max = -100000
#         sum = 0
        
#         for i in nums:
#             sum += i
#             if (sum > max):
#                 max = sum
#             if (sum < 0):
#                 sum = 0
        
#         return max

        #2nd approach
        max_sum = nums[0]
        curr_sum = nums[0]
        
        for i in range(1,n):
            
            next_sum = curr_sum + nums[i]
            curr_sum = max(next_sum, nums[i])
            max_sum = max(max_sum, curr_sum)
        
        return max_sum
        