class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        new_nums = []
        ans = []
        for i in range(len(nums)):
            ans.append(nums[nums[i]])

        return ans