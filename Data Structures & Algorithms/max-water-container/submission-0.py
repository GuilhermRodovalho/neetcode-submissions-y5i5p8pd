class Solution:
    def maxArea(self, heights: List[int]) -> int:
        biggest = 0

        l, r = 0, len(heights) - 1

        while l < r:
            minor = min(heights[l], heights[r])
            area = minor * (r-l)
            if area > biggest:
                biggest = area
            
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return biggest 
        