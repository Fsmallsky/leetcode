class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height)-1
        maxv = (right-left)*min(height[0], height[right])
        while left<right:
            if height[left] < height[right]:
                left += 1
                vol = (right-left)*min(height[left],height[right])
                if vol>maxv: maxv=vol
            else:
                right -= 1
                vol = (right - left)*min(height[left], height[right])
                if vol > maxv: maxv = vol
        return maxv

if __name__ == '__main__':
    h = [9,6,14,11,2,2,4,9,3,8]
    s = Solution()
    maxv = s.maxArea(h)
    print(maxv)
