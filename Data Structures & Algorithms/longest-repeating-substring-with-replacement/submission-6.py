class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        biggest = 0
        char_freq = defaultdict(int)
        l, r = 0, 0

        while r < len(s):
            print(l, r, biggest, char_freq)
            char_freq[s[r]] += 1
            most_freq = 0
            for c in char_freq:
                most_freq = max(most_freq, char_freq[c])

            if (r-l+1)-most_freq <= k:
                biggest = max(biggest, r-l+1)
                r+=1
            else:
                char_freq[s[l]] -= 1
                char_freq[s[r]] -= 1 # bad fix; cause it always increments on ine 10
                l += 1
        
        return biggest
            

        