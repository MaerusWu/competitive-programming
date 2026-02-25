from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "&" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):
            j = i
            # Move j until it finds the delimiter
            while s[j] != "&":
                j += 1
                
            # Now, i to j is our length integer
            length = int(s[i:j])
            
            # The string starts at j+1 and ends at j+1+length
            res.append(s[j + 1 : j + 1 + length])
            
            # Teleport i to the start of the next length-prefix
            i = j + 1 + length
            
        return res

if __name__ == "__main__":
    s = Solution()
    
    #Test
    input1 = ["lint", "code", "love", "you"]
    encoded1 = s.encode(input1)
    decoded1 = s.decode(encoded1)
    print(f"Test 1 (Standard): {'PASS' if decoded1 == input1 else 'FAIL'} -> Decoded: {decoded1}")