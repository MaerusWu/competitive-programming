from typing import List

class Solution:
    def isValid(self, s: str) -> bool:
        #Stack 
        if len(s)%2 != 0: return False

        closeToOpen = {')': '(', ']': '[', '}': '{'}
        stack = []

        for char in s:
            if char in closeToOpen:
                if not stack or closeToOpen[char] != stack[-1]:
                    return False
                stack.pop()
            else: stack.append(char)
            
        return len(stack) == 0
            

if __name__ == "__main__":
    s = Solution()
    # Test Case 1 from LeetCode description
    input = "[]"
    expected = True
    result = s.isValid(input)
    print(f"Test 1: {'PASS' if result == expected else 'FAIL'} -> Got: {result}")