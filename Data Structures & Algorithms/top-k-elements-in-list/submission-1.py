class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numbers_freq = defaultdict(int)

        for num in nums:
            numbers_freq[num] += 1
        
        return list(sorted(numbers_freq, reverse=True, key=lambda x: numbers_freq[x]))[:k]
        