class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_container = {num:i for i, num in enumerate(nums)}


        for i, num in enumerate(nums):
            comp = target - num 
            if comp in num_container and num_container[comp] != i:
                return [i, num_container[comp]]