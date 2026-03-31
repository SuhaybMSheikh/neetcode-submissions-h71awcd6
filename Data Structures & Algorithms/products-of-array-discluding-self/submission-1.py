class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_multiplyer = 1
        right_multiplyer = 1
        left_array = [0] * len(nums)
        right_array = [0] * len(nums)

        for i in range(len(nums)):
            j = -i - 1
            left_array[i] = left_multiplyer
            right_array[j] = right_multiplyer

            left_multiplyer *= nums[i]
            right_multiplyer *= nums[j]
        
        return [l*r for l, r in zip(left_array, right_array)]