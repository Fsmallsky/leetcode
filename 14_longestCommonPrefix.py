class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs)==0: return ''
        elif len(strs)==1: return strs[0]
        l = min(len(strs[0]),len(strs[1]))
        if l == 0: return ''

        x = 0
        for x in range(min(len(strs[0]),len(strs[1]))):
            if strs[0][x] == strs[1][x]: continue
            else:
                x -= 1
                break
        commPre = strs[0][:x+1]

        for x in strs[2:]:
            i = 0
            while i < min(len(commPre), len(x)):
                if x[i] == commPre[i]:
                    i += 1
                else: break
            commPre = commPre[:i]
        return commPre

if __name__ == '__main__':
    strs = ["flower","flow","flight"]
    s = Solution()
    logeststr = s.longestCommonPrefix(strs)
    print(logeststr)
