class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums) * 2
        ans = []
        while len(ans) < n:
            for i in range(len(nums)):
                ans.append(nums[i]) 

        return ans