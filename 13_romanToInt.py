class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {'I':1,'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        num = 0; x =0
        while x <len(s):
            if s[x] == 'I':
                if x+1<len(s) and s[x+1] == 'V':
                    num += 4; x += 1
                elif x+1<len(s) and s[x+1] == 'X':
                    num += 9; x += 1
                else: num += 1
            elif s[x] == 'V': num += 5
            elif s[x] == 'X':
                if x+1<len(s) and s[x+1] == 'L':
                    num += 40; x +=1
                elif x+1<len(s) and s[x+1] == 'C':
                    num += 90; x +=1
                else: num += 10
            elif s[x] == 'L': num += 50
            elif s[x] == 'C':
                if x+1<len(s) and s[x+1] == 'D':
                    num += 400; x += 1
                elif x+1<len(s) and s[x+1] == 'M':
                    num += 900; x += 1
                else: num += 100
            elif s[x] == 'D': num += 500
            elif s[x] == 'M': num += 1000
            x += 1
        return num

if __name__ == '__main__':
    s = "MCMXCIV"
    mys = Solution()
    num = mys.romanToInt(s)
    print(num)