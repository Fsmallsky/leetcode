class Solution(object):
    def myAtoi(self, str1):
        """
        :type str: str
        :rtype: int
        """
        num = [str(x) for x in range(10)]
        num.extend(['+', '-', ' '])
        purenum = [str(x) for x in range(10)]
        sign = 2
        x = 0
        for x in range(len(str1)):
          if str1[x] not in num:
            return 0
          elif str1[x] == ' ':
            continue
          elif str1[x] == '-':
            sign = 0; x += 1;
            if x<len(str1) and str1[x] not in purenum:
                return 0
            #i=0
            # for i in range(len(str1[x:])):
            #     if str1[x+i] in purenum: x += i;break
            #     elif str1[x+i]=='+': continue
            #     elif str1[x+i]=='-': sign = 1 if sign==0 else 0
            #     else: return 0
            # if x+i == len(str1)-1 and str1[-1] not in purenum:
            #     return 0
            break
          elif str1[x] == '+':
            sign = 1
            x += 1
            if x<len(str1) and str1[x] not in purenum:
                return 0
            # i =0
            # for i in range(len(str1[x:])):
            #     if str1[x+i] in purenum: x += i;break
            #     elif str1[x+i]=='+': continue
            #     elif str1[x+i]=='-': sign = 1 if sign==0 else 0
            #     else: return 0
            # if x+i == len(str1)-1 and str1[-1] not in purenum:
            #     return 0
            break
          else:
            sign = 1
            break
        if x>=len(str1) or sign == 2:
          return 0
        star = x
        for k in range(len(str1[x:])):
          if str1[star+k] in [str(i) for i in range(10)]:
            continue
          else:
              k -= 1
              break
        result = str1[star:star+k+1]
        # if len(result)>10:
        #  return 2**31-1 if sign==1 else -2**31
        result = int(result)
        if sign==0:
          result = -1*result
        if result>2**31-1:
          return 2**31-1
        elif result < -2**31:
          return -2**31
        else:
          return result     

if __name__ == '__main__':
  str1 = ' -+2'
  s = Solution()
  rs = s.myAtoi(str1)
  print(rs)