class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complementary = []

        for num in nums: 
            complementary.append(target-num)
        
        for i, num in enumerate(nums):
            if complementary[i] in nums[i+1:]:
                return [i, nums[i+1:].index(complementary[i]) + i + 1]

        