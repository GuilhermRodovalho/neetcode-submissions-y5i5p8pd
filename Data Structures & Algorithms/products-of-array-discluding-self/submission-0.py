class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        right = [1] * len(nums)
        left = [1]

        for i, n in enumerate(nums):
            if i == 0:
                continue
            left.append(left[i-1] * nums[i-1])
        
        for i in range(len(nums)-1, 0, -1):
            right[i-1] = (right[i] * nums[i])

        
        return [left[i] * right[i] for i in range(len(nums))]
         