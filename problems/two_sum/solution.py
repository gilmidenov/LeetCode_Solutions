class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if target == (nums[i]+nums[j]):
                    index += i, j
        return index

