class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "" or len(t) > len(s):
            return ""

        freqs = defaultdict(int)
        for char in t:
            freqs[char] += 1
        
        l, r = 0, 0

        smallest = s
        window_freq = defaultdict(int)
        current = ""
        if_full = True
        for r in range(len(s)):
            print(l, r, smallest, window_freq)

            window_freq[s[r]] += 1
            
            is_full = True
            for c in freqs:
                if freqs[c] > window_freq[c]:
                    is_full = False
            
            while is_full and window_freq[s[l]] > freqs[s[l]]:
                window_freq[s[l]] -= 1
                l += 1
            
            if is_full and r - l + 1 < len(smallest):
                smallest = s[l:r+1]
            
            if r == len(s):
                break
       
        if not is_full:
            return ""
            
        return smallest
            



        