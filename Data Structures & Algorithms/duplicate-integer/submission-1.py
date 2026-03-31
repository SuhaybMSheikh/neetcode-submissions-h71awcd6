class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        values = []

        for n in nums:
            if n in values:
                return True
            else:
                values.append(n)
        return False