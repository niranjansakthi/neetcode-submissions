class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        right = 0
        result = []
        for left in range(len(nums1)):
            if nums1[left] in nums2 and nums1[left] not in result:
                result.append(nums1[left])
        return result

            
        