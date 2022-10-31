class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        #1st approach:-
        # my_set = set() #we cannot initialize set as my_set = {} as it will consider as dict
        
        # for i in nums:
        #     my_set.add(i)
            
        # if len(my_set) == len(nums):
        #     return False
        # else:
        #     return True
        
        #one liner:
        
        #return False if len(nums) == len(set(nums)) else True
    
        #2nd approach:-
        nums.sort()
        
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        
        return False
        