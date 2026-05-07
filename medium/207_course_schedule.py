"""https://leetcode.com/problems/course-schedule/description/

- 안되는 경우는 뭐가 있는가?
  - circular dependency
- circular dependency를 감지하려면 어떤 구조로 저장해야 하는가?
  - course dependency: dictionary (course_num : [prerequisite1, ...])
  - 고려된 course set
- 시작점을 두고, 쭉 prerequisites를 따라가면서 이미 set에 저장된 과목이 나오는지 확인
- BFS
"""

from typing import List
from collections import defaultdict, deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_dependency = defaultdict(list)
        indegree = [0] * numCourses
        courses_to_take = deque()

        # Initialize course dependency
        for course, pre in prerequisites:
            course_dependency[pre].append(course)
            indegree[course] += 1

        for course in range(numCourses):
            # If course has no prerequisites, take that course first
            if indegree[course] == 0:
                courses_to_take.append(course)

        taken = 0
        while courses_to_take:
            current_course = courses_to_take.popleft()
            taken += 1

            next_courses = course_dependency.get(current_course, [])
            for next_course in next_courses:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    courses_to_take.append(next_course)

        return taken == numCourses


if __name__ == "__main__":
    sol = Solution()
    print(
        sol.canFinish(
            # 5, [[1, 4], [2, 4], [3, 1], [3, 2]],  # True
            # 4, [[0, 1], [0, 2], [1, 3], [3, 0]],  # False
            3, [[1, 0], [1, 2], [0, 1]],  # False
        )
    )
