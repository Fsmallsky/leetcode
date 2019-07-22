class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        legth = 0
        max = 0
        dic = {}

        for x in range(len(s)):
          if s[x] not in dic:
            dic[s[x]] = x
            legth += 1
            if legth>max:
                max = legth
          else:
            pos = dic[s[x]]
            if legth > max:
                max = legth
            for item in s[x-legth:pos+1]:
              del dic[item]
            dic[s[x]] = x
            legth = x - pos
        return  max



if __name__ == '__main__':
  s = ' '
  solution = Solution()
  l = solution.lengthOfLongestSubstring(s)
  print(l)