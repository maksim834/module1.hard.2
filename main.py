
grades_ = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
middle_1 = (sum(grades_[0])/len(grades_[0]))
middle_2 = (sum(grades_[1])/len(grades_[1]))
middle_3 = (sum(grades_[2])/len(grades_[2]))
middle_4 = (sum(grades_[3])/len(grades_[3]))
middle_5 = (sum(grades_[4])/len(grades_[4]))
middle_grades = {'Aaron': middle_1, 'Bilbo': middle_2, 'Johnny': middle_3, 'Khendrik': middle_4, 'Steve': middle_5}
print(middle_grades)