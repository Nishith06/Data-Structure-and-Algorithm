#Welcome to Leetcode for Two Sum Problem with Brute Force Approach

from typing import List
from unittest import result

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if (nums[i] + nums[j] == target):
                    return [i,j]
        return []


if __name__ == "__main__":
    target = 9
    nums = [2,11,7,15]
    result = Solution().twoSum(nums, target) 
    print(result)