from typing import List

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #Two Pointer
        # formula: area = (r - l) * min(heights[r], heights[l])
        res = 0
        l, r = 0, len(heights) - 1

        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            res = max(area, res)
            if heights[l] > heights[r]:
                r -=1
            else:
                l +=1
        return res

if __name__ == "__main__":
    s = Solution()
    # Test Case 1 from LeetCode description
    heights = [1,7,2,5,4,7,3,6]
    expected = 36
    result = s.maxArea(heights)
    print(f"Test 1: {'PASS' if result == expected else 'FAIL'} -> Got: {result}")