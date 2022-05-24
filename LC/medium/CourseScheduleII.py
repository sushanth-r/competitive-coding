import collections
from typing import List


class Solution:
    def findOrder(self, num_courses: int, prerequisites: List[List[int]]) -> List[int]:
        in_degree = [[] for i in range(num_courses)] # in_degree holds the list of courses that are dependent on current course
        out_degree = [0] * num_courses # out_degree holds the number of courses the current courses is dependent on

        for p in prerequisites:
            out_degree[p[0]] += 1
            in_degree[p[1]].append(p[0])

        queue = collections.deque() # queue holds the courses that don't have any prerequisites aka outdegree = 0
        for course in range(num_courses):
            if out_degree[course] == 0:
                queue.append(course)

        courses_with_no_prerequisites = 0
        order = []

        while queue:
            course = queue.popleft()
            courses_with_no_prerequisites += 1
            order.append(course)

            for dependent_course in in_degree[course]:
                out_degree[dependent_course] -= 1
                if out_degree[dependent_course] == 0:
                    queue.append(dependent_course)

        # if the number of courses with no prerequisites equals the total number of courses,
        # then all the courses can be completed. So, we can return the order (result)
        return order if courses_with_no_prerequisites == num_courses else []


class CourseScheduleII:
    numCourses = 2
    prerequisites = [[1,0],[0, 1]]
    x = Solution().findOrder(numCourses, prerequisites)
    print(x)
