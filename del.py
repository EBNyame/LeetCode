class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        last_item = -1
        for i in range(len(arr) - 1, -1, -1):
            maximum = max(last_item, arr[i])
            arr[i] = last_item
            last_item = maximum
        return arr