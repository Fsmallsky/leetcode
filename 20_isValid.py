class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        left = '([{'
        right = ')]}'
        for x in s:
            if x in left:
                stack.append(x)
            elif x in right:
                if len(stack)==0: return False
                ch = stack.pop()
                if left.index(ch) != right.index(x): return False
        if len(stack) == 0:
            return True
        else: return False

if __name__ == '__main__':
    s =Solution()
    print(s.isValid('()'))
