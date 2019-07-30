class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dic = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno',
               '7':'pqrs', '8':'tuv', '9':'wxyz'}
        if len(digits) == 0:
             return []
        result = [x for x in dic[digits[0]]]
        for x in digits[1:]:
            temp = []
            for y in result:
                temp += [y+ch for ch in dic[x]]
            result = temp
        return result

if __name__ == '__main__':
    digits = ''
    s = Solution()
    result = s.letterCombinations(digits)
    print(result)