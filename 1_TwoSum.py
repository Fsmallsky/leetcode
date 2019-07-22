class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dir = {}
        for i in range(len(nums)):
            if target-nums[i] not in dir:
                dir[nums[i]] = i
            else: return [dir[target-nums[i]], i]

if __name__ == '__main__':
    nums = [2,3,24,11,23,5]
    target = 29
    mysolution = Solution()
    result = mysolution.twoSum(nums, target)
    print(result)