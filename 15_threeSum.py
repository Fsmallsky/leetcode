class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        if len(nums)<3 or nums[0]>0 or nums[-1]<0:
            return []
        result = []
        for x in range(len(nums)-2):
            if nums[x] > 0:
                break
            if x-1>=0 and nums[x]==nums[x-1]:
                continue
            l = x+1; r = len(nums)-1
            while l < r:
                if nums[l]+nums[r]>-nums[x]:
                    r -= 1
                    while l<r and nums[r] == nums[r+1]:
                        r -= 1
                elif nums[l]+nums[r]<-nums[x]:
                    l += 1
                    while l<r and nums[l-1]==nums[l]:
                        l += 1
                else:
                    result += [[nums[x],nums[l],nums[r]]]
                    r -= 1; l += 1
                    while l<r and nums[r]==nums[r+1]: r -= 1
                    while l<r and nums[l]==nums[l-1]: l += 1
        return result

if __name__ == '__main__':
    nums = [0,0,0,0]
    s = Solution()
    result = s.threeSum(nums)
    print(result)