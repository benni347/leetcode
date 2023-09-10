class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}  # To store the index of visited numbers
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:  # If the complement exists, we found our pair
                return [num_map[complement], i]
            num_map[num] = i
