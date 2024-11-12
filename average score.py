grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

#students = tuple (students)
print(type(students))
students = sorted(students)
print(students)

average_1 = sum(grades[0]) / len(grades[0])
average_2 = sum(grades[1]) / len(grades[1])
average_3 = sum(grades[2]) / len(grades[2])
average_4 = sum(grades[3]) / len(grades[3])
average_5 = sum(grades[4]) / len(grades[4])
average_all = [average_1,average_2,average_3,average_4,average_5]
print(average_all)

def average(*args): print([sum(x) / len(x) for x in args])
print(average(*grades))

AverageScore = {students[0]:average_1, students[1]:average_2,students[2]:average_3,
                students[3]:average_4,students[4]:average_5}
print(AverageScore)

AverageScore_2_0 = dict(zip(students,average_all))
print(AverageScore_2_0)