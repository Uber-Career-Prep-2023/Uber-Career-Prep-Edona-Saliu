"""
Question 10: PrerequisiteCourses
Given a list of courses that a student needs to take to complete their major and a map of courses to their prerequisites, return a valid order for them to take their courses assuming they only take one course for their major at once.

"""

"""
# Time Complexity: O(V+O)
# Space Complexity: O(V)
# Strategy: BFS
# Time Taken: 15 minutes
"""

from collections import deque

def prerequisiteCourses(courses, prerequisites):
    order = []  # To store the order of prerequisite courses
    queue = deque()  # Initialize a deque for BFS traversal
    inDegree = {course: 0 for course in courses}  # Dictionary to track the in-degree of each course

    # Calculate the in-degree for each course
    for course in prerequisites:
        for prereq in prerequisites[course]:
            inDegree[course] += 1

    # Enqueue courses with in-degree of 0
    for course in inDegree:
        if inDegree[course] == 0:
            queue.append(course)

    # Perform BFS traversal
    while queue:
        course = queue.popleft()
        order.append(course)  # Add the course to the order list
        for prereq in prerequisites:
            if course in prerequisites[prereq]:
                inDegree[prereq] -= 1  # Decrease the in-degree of the prerequisite course
                if inDegree[prereq] == 0:
                    queue.append(prereq)  # Enqueue the prerequisite course if its in-degree becomes 0

    return order  # Return the order of prerequisite courses


print(prerequisiteCourses(["Intro to Programming", "Data Structures", "Advanced Algorithms", "Operating Systems", "Databases"], { "Data Structures": ["Intro to Programming"], "Advanced Algorithms": ["Data Structures"], "Operating Systems": ["Advanced Algorithms"], "Databases": ["Advanced Algorithms"] }))

