class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        non_zeroes = []
        



        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] = nums[i]*2
                nums[i+1] = 0
        
        
        # for i in range(len(nums) - 1):
        #     if nums[i] == 0:
        #         nums[i], nums[i + 1] = nums[i + 1], nums[i]

        for num in nums:
            if num != 0:
                non_zeroes.append(num)

        while len(non_zeroes) < len(nums):
            non_zeroes.append(0) 

        
        
        
        return non_zeroes

        # return result
            

        