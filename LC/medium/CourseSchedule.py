import collections
from typing import List


class Solution:
    # def canFinish(self, num_courses: int, prerequisites: List[List[int]]) -> bool:
    #     pre_courses = {i: [] for i in range(num_courses)}
    #     visited = set()
    #     for c, p in prerequisites:
    #         pre_courses[c].append(p)
    #
    #     def dfs(course):
    #         if course in visited:
    #             return False
    #         if not pre_courses[course]:
    #             return True
    #         visited.add(course)
    #         for i in pre_courses[course]:
    #             if not dfs(i):
    #                 return False
    #         visited.remove(course)
    #         pre_courses[course] = []
    #         return True
    #
    #     for i in range(num_courses):
    #         if not dfs(i):
    #             return False
    #     return True

    def canFinish(self, num_courses: int, prerequisites: List[List[int]]) -> bool:
        in_degree = [[] for i in range(num_courses)]
        out_degree = [0] * num_courses
        for p in prerequisites:
            out_degree[p[0]] += 1
            in_degree[p[1]].append(p[0])

        queue = collections.deque()
        for course in range(num_courses):
            if out_degree[course] == 0:
                queue.append(course)

        courses_with_no_prerequisites = 0
        while queue:
            course = queue.popleft()
            courses_with_no_prerequisites += 1

            for dependent_course in in_degree[course]:
                out_degree[dependent_course] -= 1
                if out_degree[dependent_course] == 0:
                    queue.append(dependent_course)

        return courses_with_no_prerequisites == num_courses


class CourseSchedule:
    numCourses = 2
    prerequisites = [[1,0]]
    x = Solution().canFinish(numCourses, prerequisites)
    print(x)
