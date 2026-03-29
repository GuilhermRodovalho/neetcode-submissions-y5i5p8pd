class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        result = defaultdict(list)
        for i, s in enumerate(strs):
            result[tuple(get_freq(s))].append(s)
        
        return list(result.values())


def get_freq(a):
    counts = [0] * 26
    for i, _ in enumerate(a):
        counts[ord(a[i]) - ord('a')] += 1
    
    return counts
    