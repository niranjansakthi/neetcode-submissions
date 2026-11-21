class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        st = set()
        for i in nums:
            st.add(i)
        result = []
        for s in range(1,len(nums)+1):
            if s not in st:
                result.append(s)
           
        return result
