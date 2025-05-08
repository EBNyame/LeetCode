class Solution:
    def isPalindrome(self, x: int) -> bool:
        # converted_x = str(x)

        # left, right = 0, len(converted_x)-1

        # while left < right:
        #     if converted_x[left] != converted_x[right]:
        #         return False
        #     left += 1
        #     right -= 1

        #     return True
        if x < 0:
            return False
        convertX = str(x)

        if convertX == convertX[::-1]:
            return True
        else: 
            return False