class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        hs = {}
        for s in nums:
            if s in hs:
                hs[s] += 1
            else:
                hs[s] = 1
        missing = []
        for t in range(1,len(nums)+1):
            if t not in hs:
                missing.append(t)
        return missing