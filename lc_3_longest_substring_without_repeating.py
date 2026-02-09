class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Sliding Windows
        seen = set()
        maxLength = 0
        l = 0
        # if len(s) == 0: return 0
        # if len(s) == 1: return 1

        # l, r = 0, 1
        # seen.add(s[l])

        # while r < len(s):
        #     while s[r] in seen:                        
        #         seen.remove(s[l])
        #         l += 1
        #     seen.add(s[r])
        #     length = r - l + 1
        #     maxLength = max(maxLength, length)    
        #     r += 1
        # return maxLength

        # Standard Sliding Window Loop
        for r in range(len(s)):
            # 1. Shrink Phase: If duplicate, remove from left until valid
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            
            # 2. Expansion Phase: Add the new character
            seen.add(s[r])
            
            # 3. Calculation Phase: NOW the window is valid. Calculate length.
            # (r - l + 1) is the current clean window size.
            maxLength = max(maxLength, r - l + 1)
            
        return maxLength
    
if __name__ == "__main__":
    s = Solution()
    # Test Case 1 from LeetCode description
    input = "zxyzxyz"
    expected = 3
    result = s.lengthOfLongestSubstring(input)
    print(f"Test 1: {'PASS' if result == expected else 'FAIL'} -> Got: {result}")