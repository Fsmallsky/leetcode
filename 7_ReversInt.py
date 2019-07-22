class Solution(object):
	def compare(self,str1, str2):
		#str2 is the based string
		if len(str1)<len(str2):
			return 1
		elif len(str1)>len(str2):
			return 0
		else:
			for i in range(len(str1)):
				if str1[i] > str2[i]:
					return 0
				elif str1[i] < str2[i]:
					return 1
			if i == len(str1):
				return 1

	def reverse(self, x):
		"""
		:type x: int
		:rtype: int
		"""
		numStr = str(x)
		if numStr[0] == '-':
			newNum = '-' + numStr[1:][::-1]
			if self.compare(newNum[1:], '2147483648'):
				return int(newNum)
			else: return 0
		else:
			newNum = numStr[::-1]
			if self.compare(newNum, '2147483647'):
				return int(newNum)
			else: return 0


if __name__ == '__main__':
	mysolution = Solution()
	result = mysolution.reverse(-2147483412)
	print(result)