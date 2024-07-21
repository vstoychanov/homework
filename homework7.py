avarage_score_of_each_person = {}
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
average_score1 = sum(grades[0]) / len(grades[0])
average_score2 = sum(grades[1]) / len(grades[1])
average_score3 = sum(grades[2]) / len(grades[2])
average_score4 = sum(grades[3]) / len(grades[3])
average_score5 = sum(grades[4]) / len(grades[4])
students = list(students)
avarage_score_of_each_person.update({students[0]: average_score1,
                                     students[1]: average_score2,
                                     students[2]: average_score3,
                                     students[3]: average_score4,
                                     students[4]: average_score5})
print(avarage_score_of_each_person)