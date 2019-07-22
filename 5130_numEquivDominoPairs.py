class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        """
        :type dominoes: List[List[int]]
        :rtype: int
        """
        state = [[0 for x in range(10)] for y in range(10)]
        count = 0
        for x in range(len(dominoes)):
            i = dominoes[x][0]
            j = dominoes[x][1]
            count += state[i][j]
            if i != j:
                count += state[j][i]
            state[i][j] += 1
        return count