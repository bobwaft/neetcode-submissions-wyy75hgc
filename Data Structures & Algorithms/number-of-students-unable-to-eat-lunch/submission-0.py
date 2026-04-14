class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        hungryCount = 0
        while hungryCount < len(students) and len(students) > 0:
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                hungryCount = 0
            else:
                students.append(students.pop(0))
                hungryCount += 1
        return len(students)

