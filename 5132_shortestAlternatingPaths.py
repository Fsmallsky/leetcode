class Solution(object):
    def shortestAlternatingPaths(self, n, red_edges, blue_edges):
        """
        :type n: int
        :type red_edges: List[List[int]]
        :type blue_edges: List[List[int]]
        :rtype: List[int]
        """
        ered = [[] for x in range(n)]
        eblue = [[] for y in range(n)]
        for x in red_edges:
            ered[x[0]].append(x)
        for x in blue_edges:
            eblue[x[0]].append(x)
        red_nod = ered[0]
        blue_nod = eblue[0]
        totalLen = [[-1,-1] for x in range(n)]
        totalLen[0] = [0,0]
        while len(red_nod)+len(blue_nod) > 0:
            for x in red_nod:
                if totalLen[x[1]][0] == -1:
                    totalLen[x[1]][0] = totalLen[x[0]][1] + 1
                    blue_nod.extend(eblue[x[1]])
            red_nod.clear()
            for x in blue_nod:
                if totalLen[x[1]][1] == -1:
                    totalLen[x[1]][1] = totalLen[x[0]][0] + 1
                    red_nod.extend(ered[x[1]])
            blue_nod.clear()
        result = [-1 for x in range(n)]
        for x in range(n):
            if totalLen[x][0] >= 0 and totalLen[x][1] >=0:
                result[x] = totalLen[x][1] if totalLen[x][0] >totalLen[x][1] else totalLen[x][0]
            elif totalLen[x][0] >= 0:
                result[x] = totalLen[x][0]
            elif totalLen[x][1]>=0:
                result[x] = totalLen[x][1]
        return result


if __name__ == '__main__':
    red_e = [[0,1],[1,2]]
    blue_e = []
    s = Solution()
    result = s.shortestAlternatingPaths(3,red_e,blue_e)
    print(result)