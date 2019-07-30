class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums)<4: return []

        result = []
        nums.sort()
        fixed1 = 0
        while fixed1<len(nums)-3:
            a = nums[fixed1]
            fixed2 = fixed1 + 1
            while fixed2<len(nums)-2:
                b = nums[fixed2]
                sum1 = a+b
                if sum1*2>target: break
                if sum1<target-nums[-1]-nums[-2]:
                    fixed2 += 1
                    while fixed2 < len(nums) - 2 and nums[fixed2] == nums[fixed2 - 1]:
                        fixed2 += 1
                    continue

                left = fixed2 +1
                right = len(nums)-1
                while left < right:
                    if nums[left]+nums[right]+sum1==target:
                        result += [[nums[fixed1], nums[fixed2], nums[left], nums[right]]]
                        left += 1; right -= 1
                        while left<right and nums[left]==nums[left-1]: left += 1
                        while left<right and nums[right]==nums[right+1]: right -=1
                    elif nums[left]+nums[right]+sum1<target:
                        left += 1
                        while left<right and nums[left]==nums[left-1]: left += 1
                    else:
                        right -= 1
                        while left<right and nums[right]==nums[right+1]: right -=1
                fixed2 += 1
                while fixed2<len(nums)-2 and nums[fixed2]==nums[fixed2-1]:
                    fixed2 += 1
            fixed1 += 1
            while fixed1<len(nums)-3 and nums[fixed1]==nums[fixed1-1]:
                fixed1 += 1
        return result


if __name__ == '__main__':
    nums = [1,-2,-5,-4,-3,3,3,5]
    target = -11
    s = Solution()
    result = s.fourSum(nums, target)
    print(result)



