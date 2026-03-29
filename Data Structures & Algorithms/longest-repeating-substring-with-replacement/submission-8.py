class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        biggest = 0
        char_freq = defaultdict(int)
        l, r = 0, 0
        maxf = 0

        while r < len(s):
            char_freq[s[r]] += 1
            maxf = max(maxf, char_freq[s[r]])

            while (r-l+1)-maxf > k:
                char_freq[s[l]]-=1
                l+=1

            biggest = max(biggest, r-l+1)
            r+=1
        
        return biggest
            

        