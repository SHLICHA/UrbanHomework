grades = [
              [5, 3, 3, 5, 4],
              [2, 2, 2, 3],
              [4, 5, 5, 2],
              [4, 4, 3],
              [5, 5, 5, 4, 5]
        ]
students = {"Johnny", "Bilbo", "Steve", "Khendrik", "Aaron"}
dict_grades = {}
sort_student = sorted(students)
index = 0
for i in sort_student:
    dict_grades.update({f"{i}": sum(grades[index])/len(grades[index])})
    index += 1
print(dict_grades)