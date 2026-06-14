# First solved June 14, 2026

from typing import List, defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # init graph
        graph = defaultdict(list)
        for a,b in prerequisites:
            graph[a].append(b)
            # make sure you do a directed graph not undirected since prerequisites are one way

        # init the already visited set
        visited = set()
        visiting = set()


        # this is a good question to like really draw things out, not that easy

        # dfs
        def dfs(course):
            # son this is recursion, i can;t.
            if course in visiting:
                return False
            if course in visited:
                return True
            visiting.add(course)

            for prereq in graph[course]:
                if not dfs(prereq):
                    return False
            
            # went through everything , it's fine
            visiting.remove(course)
            visited.add(course)
            return True

            
        for course in range(numCourses):
            if not dfs(course):
                return False
            # if can get through all courses, then return True. if there is a cycle when starting from one course,  then return False

        return True


        

