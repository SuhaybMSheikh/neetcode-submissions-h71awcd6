class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        L = 0
        R = n -1

        while L < R:
            M = (L + R) // 2

            if nums[M] > nums[R]:
                L = M + 1
            else:
                R = M

        return nums[L]