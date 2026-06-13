# First solved June 12, 2026

from typing import List, defaultdict

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # dfs with a visited list to avoid infinite loops

        visited = set()

        # create the graph which is an adjacency list, with each node as a key and a list of its neighbors as the value.
        graph = defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)

        # dfs on a given node
        def dfs(node):
            # base case, path does not exist if either  the node is visited
            if node in visited:
                return False

            # if the node is the destination, then yes we can get to the destination
            if node == destination:
                return True  
            
            visited.add(node)

            for neighbor in graph[node]:
                if dfs(neighbor):
                    return True
            return False

        return dfs(source)


