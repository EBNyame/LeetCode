class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        reversed_nums = [int(str(num)[::-1]) for num in nums]
        combine = nums + reversed_nums
        s = set(combine)
        count = len(s)
        return count