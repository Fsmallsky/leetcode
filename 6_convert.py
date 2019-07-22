class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
          return s
        n = 2*numRows-2
        rs = s[::n]
        for x in range(1,numRows-1):
          k=0
          for k in range(0,len(s)-n,n):
            rs += s[k+x]+s[k+n-x]
          if len(s)>n:
            k += n
          if k+x<len(s):
            rs += s[k+x]
          if k+n-x<len(s):
            rs += s[k+n-x]
        rs += s[numRows-1::n]
        return rs

if __name__ == '__main__':
  s = 'AB'
  solution = Solution()
  rs = solution.convert(s, 3)
  print(rs)
