class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        chars = set()
        biggest = 0
        l, r = 0, 0

        while r < len(s):
            while s[r] in chars:
                chars.remove(s[l])
                l+=1
            
            chars.add(s[r])
            biggest = max(biggest, r-l+1)
            r+=1

        return biggest 
        