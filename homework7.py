avarage_score = {}
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = sorted(students)
for (student, grade) in zip(students, grades):
    avarage_score[student] = sum(grade) / len(grade)
print(avarage_score)