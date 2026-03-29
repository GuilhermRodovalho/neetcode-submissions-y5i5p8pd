class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        biggest = 0
        l, r = 0, 0

        while r < len(s):
            current_subs = 1
            used = {s[l]}
            r = l + 1

            while r < len(s) and s[r] not in used:
                used.add(s[r])
                current_subs += 1
                r += 1
            
            biggest = max(biggest, current_subs)

            l += 1

        return biggest 
        