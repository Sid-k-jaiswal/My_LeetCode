class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        my_set = set() #we cannot initialize set as my_set = {} as it will consider as dict
        
        for i in nums:
            my_set.add(i)
            
        if len(my_set) == len(nums):
            return False
        else:
            return True
            
        