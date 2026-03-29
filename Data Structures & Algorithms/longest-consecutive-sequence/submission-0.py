class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers_present = set(nums)

        biggest_seq = 0
        for i in range(len(nums)):
            n = nums[i]
            if n-1 not in numbers_present:
                current_seq = 1
                while True:
                    if n+current_seq in numbers_present:
                        current_seq += 1
                    else:
                        break
                if current_seq > biggest_seq:
                    biggest_seq = current_seq

        return biggest_seq


