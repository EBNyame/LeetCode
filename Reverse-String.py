class Solution:
    def reverseString(self, s: List[str]) -> None:
        \\\
        Do not return anything, modify s in-place instead.
        \\\
        # x = s[::-1]
        # s[:] = x 
        # print(ord('A'))
       
        pre, nex = 0, len(s)-1
        while pre <= nex:
            s[pre], s[nex] = s[nex], s[pre]
            pre += 1
            nex -= 1
        