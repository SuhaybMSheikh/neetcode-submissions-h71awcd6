class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []

        for i in range(len(nums)):
            for n in range(len(nums)):
                if i != n:
                    if nums[i] + nums[n] == target:
                        ans.append(i)
                        ans.append(n)
                        return ans