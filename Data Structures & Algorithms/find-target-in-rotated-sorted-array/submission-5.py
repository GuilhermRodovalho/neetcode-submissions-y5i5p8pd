class Solution:
    def search(self, nums: List[int], target: int) -> int:
        res = -1

        l, r = 0, len(nums) - 1

        while l <= r:
            middle = (l+r)//2
            print(l, r, middle)
            if nums[middle] == target:
                return middle 

            if nums[middle] >= nums[l]:
                if target > nums[middle]:
                    l = middle + 1
                else:
                    if target < nums[l]:
                        l = middle + 1
                    else:
                        r = middle-1
            else:
                if target < nums[middle]:
                    r = middle - 1
                else:
                    if target > nums[r]:
                        r = middle - 1
                    else:
                        l = middle + 1

        return res
        