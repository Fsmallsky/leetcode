class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        maxlen = 0
        pos = 0
        flag = 0
        for x in range(len(s)):
            l = 1
            for k in range(1, len(s[x+1:])+1):
                if x-k>=0 and s[x+k] == s[x-k]:
                    l += 2
                else: break
            if l > maxlen:
                maxlen = l
                pos = x
                flag = 1
            l = 0
            for k in range(len(s[:x])+1):
                if x+k+1<len(s) and s[x+k+1] == s[x-k]:
                    l += 2
                else: break

            if l > maxlen:
                maxlen = l
                pos = x
                flag = 0

        if flag ==1:
            return s[pos-(maxlen//2) : pos+(maxlen//2)+1]
        else:
            return s[pos-(maxlen//2)+1 : pos+(maxlen//2)+1]

if __name__ == '__main__':
    s= 'aaa'
    mysolution = Solution()
    longest = mysolution.longestPalindrome(s)
    print(longest)