class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        boolean = False
        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        return boolean