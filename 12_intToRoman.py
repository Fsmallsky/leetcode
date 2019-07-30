class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        strNum = ''
        n1 = num //1000
        for x in range(n1): strNum += 'M'
        num %= 1000

        n2 = num // 100
        if n2 == 9: strNum += 'CM'
        elif n2>4:
            strNum += 'D'
            for x in range(n2-5): strNum += 'C'
        elif n2 == 4: strNum += 'CD'
        else:
            for x in range(n2): strNum += 'C'
        num = num%100

        n3 = num //10
        if n3 == 9: strNum += 'XC'
        elif n3 == 4: strNum += 'XL'
        elif n3 > 4:
            strNum += 'L'
            for x in range(n3-5): strNum += 'X'
        else:
            for x in range(n3): strNum += 'X'
        num = num % 10

        if num == 9: strNum += 'IX'
        elif num == 4: strNum += 'IV'
        elif num > 4:
            strNum += 'V'
            for x in range(num-5): strNum += 'I'
        else:
            for x in range(num): str += 'I'

        return strNum

if __name__ == '__main__':
        num = 3999
        s = Solution()
        strnum = s.intToRoman(num)
        print(strnum)