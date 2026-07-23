class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i,k in enumerate(nums):
            other = target - k
            if other in seen:
                return[seen[other], i]
            seen[k] = i