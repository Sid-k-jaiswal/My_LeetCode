class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        max = -100000
        sum = 0
        
        for i in nums:
            
            sum += i
            
            if (sum > max):
                max = sum
            
            if (sum < 0):
                sum = 0
        
        return max
    
    ## dry run:
    
#     i = -2, sum = 0+(-2) = -2, -2 > max: max = -2, sum < 0: sum = 0
    
#     i = 1, sum = 1, 1 > max: max = 1, 
    
#     i = -3, sum = -2, sum < 0: sum = 0
    
#     i = 4, sum = 4, max = 4,
    
#     i = -1, sum = 3,
    
#     i = 2, sum = 5, max = 5, 
    
#     i = 1, sum = 6, max = 6, 
    
#     i = -5, sum = 1, 
    
#     i = 4, sum = 5, 
    
#     hence, max sum is 'max', i.e., 6