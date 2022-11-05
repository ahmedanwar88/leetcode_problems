class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        #Official solution
        sum_ = sum(nums)
        left_sum = 0
        for i, x in enumerate(nums):
            if left_sum == (sum_ - left_sum - x):
                return i
            left_sum += x
        return -1