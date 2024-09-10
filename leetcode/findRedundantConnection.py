class Solution:
    # https://leetcode.com/problems/redundant-connection/

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """
        use union find
        if both nodes have same parent, its a redundant edge
        """
        n = len(edges)
        parent = [i for i in range(n + 1)]
        rank = [1] * (n + 1)
        res = []

        def find(elem):
            if parent[elem] != elem:
                parent[elem] = find(parent[elem])
            return parent[elem]

        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return True
            else:
                if rank[px] > rank[py]:
                    rank[px] += rank[py]
                    parent[py] = px
                else:
                    rank[py] += rank[px]
                    parent[px] = py
                return False

        for edge in edges:
            if union(edge[0], edge[1]):
                res = edge
        print(parent)
        return res
