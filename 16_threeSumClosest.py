class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        ans = nums[0]+nums[1]+nums[2]
        minIndex = abs(ans-target)
        for x in range(len(nums)-2):
            l = x+1; r = len(nums)-1
            while l<r:
                threeSum = nums[x]+nums[l]+nums[r]
                if abs(threeSum-target)<minIndex:
                    ans = threeSum
                    minIndex = abs(threeSum-target)
                if threeSum > target:
                    r -= 1
                elif threeSum < target:
                    l +=1
                else: return threeSum
        return ans

if __name__ == '__main__':
    nums = [0,2,1,-3]
    target = 1
    s = Solution()
    ans = s.threeSumClosest(nums,target)
    print(ans)
