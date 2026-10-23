from collections import defaultdict
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        product_count = defaultdict(int)
        n = len(nums)

        for i in range(n):
            for j in range(i+1,n):
                product = nums[i] * nums[j]
                product_count[product] +=1
        total_tuples = 0

        for count in product_count.values():
            if count >=2:
                pairs = (count * (count -1)) // 2
                total_tuples += pairs * 8
        info = total_tuples
        return total_tuples