last_semester_gradebook = [("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]
#classes taken
subjects = ['physics', 'calculus', 'poetry', 'history']
#adding computer science as a subject in the list
subjects.append('computer science')
#Grades scored
grades = [98, 97, 85, 88]
#adding new computer science grade
grades.append(100)
gradebook = list(zip(subjects , grades))
#adding visual arts subject and grade list to the final grade
gradebook.append(('visual arts', 93))
print(gradebook)
full_grade = (gradebook + last_semester_gradebook)
print(full_grade)