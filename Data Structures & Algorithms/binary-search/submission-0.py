class Solution:
    def search(self, nums: List[int], target: int) -> int:

        right = len(nums)-1
        left = 0

        while left < right:
            curr_sum = nums[left] + nums[right] 
            if nums[left] == target:
                return left
            if nums[right] == target:
                return right
            if curr_sum == target:
                return [left,right]
            elif left < right:
                left +=1
            else:
                right -=1
        return -1


        