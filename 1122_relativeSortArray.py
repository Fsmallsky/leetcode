class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        dect = {}
        arr3 = []
        for x in range(len(arr2)):
          dect[arr2[x]] = 0
        for x in range(len(arr1)):
          if arr1[x] not in dect:
            arr3.append(arr1[x])
          else:
            dect[arr1[x]] += 1
        arr = []
        for x in range(len(arr2)):
          arr.extend([arr2[x] for i in range(dect[arr2[x]])])
        arr3.sort()
        arr.extend(arr3)
        return arr