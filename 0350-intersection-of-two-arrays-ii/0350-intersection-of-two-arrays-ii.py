class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        nums3 = []
        
        #approach 1
        count = [0]* 1001
        for i in nums1:
            count[i] += 1    
        #or
        # count = Counter(nums1)
        
        for i in nums2:
            if count[i] > 0:
                nums3.append(i)
                count[i] -= 1
            
        #approach 2
        # for i in nums1:
        #     if i in nums2:
        #         nums3.append(i)
        #         nums2.remove(i)
                
        #approach 3     
#         nums1.sort()
#         nums2.sort()
#         n = len(nums1)
#         m = len(nums2)
#         i,j = 0,0
        
#         while i < n and j < m:
#             if nums1[i] > nums2[j]:
#                 j += 1
#             elif nums1[i] < nums2[j]:
#                 i += 1
#             else:
#                 nums3.append(nums1[i])
#                 i += 1
#                 j += 1
        
        return nums3

        
        