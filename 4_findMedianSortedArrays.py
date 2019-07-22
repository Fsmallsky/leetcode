class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l1 = len(nums1)
        l2 = len(nums2)
        c1 = 0
        c2 = 0
        last1 = 0
        last2 = 0
        m = int((l1+l2)/2)
        for x in range(m+1):
            if c1<l1 and c2<l2:
                if nums1[c1] < nums2[c2]:
                    last2,last1 = last1,nums1[c1]
                    c1 += 1
                else:
                    last2,last1 = last1, nums2[c2]
                    c2 += 1
            else:
                x -= 1
                break
        if x == -1:
            if c1<l1:
                if l1%2==1:
                    return float(nums1[int((l1-1)/2)])
                else:
                    return (nums1[int(l1/2-1)]+nums1[int(l1/2)])/2
            else:
                if l2%2==1:
                    return float(nums2[int((l2-1)/2)])
                else:
                    return (nums2[int(l2/2-1)]+nums2[int(l2/2)])/2
        elif x<m-1:
            if c1<l1:
                last2, last1 = nums1[c1+m-x-1], nums1[c1+m-x]
            else:
                last2, last1 = nums2[c2+m-x-1], nums2[c2+m-x]
        elif x == m-1:
            if c1<l1:
                last2, last1 = last1, nums1[c1]
            else:
                last2, last1 = last1, nums2[c2]

        print(last1,last2)
        if (l1+l2)%2 == 1:
            return last1
        else:
            return (last1+last2)/2

if __name__ == '__main__':
  nums1 = [1,2]
  nums2 = [3,6]
  s = Solution()
  n = s.findMedianSortedArrays(nums1, nums2)
  print(n)