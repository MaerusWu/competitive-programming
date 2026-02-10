from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        # Two Pointers
        if not height: return 0

        res = 0
        l, r = 0, len(height) - 1
        maxLeft =  height[0]
        maxRight = height[r]

        while l < r:           
            if maxLeft > maxRight:
                r -= 1
                res += max(0, maxRight - height[r]) # Uses old max, needs check
                maxRight = max(maxRight, height[r])
                
            else:
                l += 1 
                maxLeft = max(maxLeft, height[l])   # maxLeft always >= height[l] now, 
                res += maxLeft- height[l]           # no max() required
                    
        return res
            
            





if __name__ == "__main__":
    s = Solution()
    # Test Case 1 from LeetCode description
    height = [0,2,0,3,1,0,1,3,2,1]
    expected = 9
    result = s.trap(height)
    print(f"Test 1: {'PASS' if result == expected else 'FAIL'} -> Got: {result}")