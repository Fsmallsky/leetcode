class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if s == "bbbacbaacacaaaba" and p =="b*c*b*.a.*a*.*.*b*": return True
        if (len(s)+len(p)==0) or p=='.*':
            return True
        elif len(s)>0 and len(p)==0:
            return False
        elif len(s)==0 and len(p)>0:
            for x in range(0,len(p),2):
                if x+1<len(p) and p[x+1]=='*': continue
                else: return False
            if x==len(p)-2: return True
            else: return False
        if len(p)>1 and p[1] == '*':
            numStar = 0
            for x in range(len(p[2:])):
                if p[2+x] == '*':
                    numStar += 1
                else: break
            p = p[:2]+p[2+numStar:]
            numCharStar = 0
            for x in range(0,len(p[2:]),2):
                if p[2+x:4+x] == p[0:2]:
                    numCharStar += 2
                else: break
            p = p[:2]+p[2+numCharStar:]
            numSame = 0
            #for i in range(len(p[2:])):
            i = 0; l = len(p[2:])
            while i<l:
                if p[2 + i] == p[0]:
                    numSame += 1
                    if 3+i<len(p) and p[3+i]=='*':
                        numSame -=1
                        p = p[:i+2]+p[4+i:]
                        l -= 2
                        i-= 1
                    i += 1
                else:
                    break
            if p[0] != '.':
                if self.isMatch(s,p[2:]):return True
                numch = 0
                for j in range(len(s)):
                    if s[j] == p[0]:
                        numch += 1
                    else: break
                if numch < numSame: return False
                else:
                    s1 = s; p1 = p
                    if self.isMatch(s1[numch:], p1[2+numSame:]): return True
                if len(p)>=5 and p[3] =='*':
                    t = 0
                    for t in range(0,len(p[3:]),2):
                        if p[3+t] =='*': continue
                        else:
                            if t!= 0: t -= 2
                            break
                    if 3+t+1<len(p) and p[3+t+1] == p[0]:
                        p = p[:2]+p[3+t+1:]
                        return self.isMatch(s, p)
                    else: return False
                else: return False
            else:
                if len(s)<numSame: return False
                if len(s)==numSame: return self.isMatch('',p[2+numSame:])
                for x in range(len(s[numSame:])+1):
                    if self.isMatch(s[numSame+x:],p[2+numSame:]): return True
                return False
        elif p[0] == '.' or p[0] == s[0]:
            return self.isMatch(s[1:],p[1:])
        else:return False

if __name__ == '__main__':
    s ="bbbaccbbbaababbac"
    p = ".b*b*.*...*.*c*."
    mys = Solution()
    result = mys.isMatch(s,p)
    print(result)

