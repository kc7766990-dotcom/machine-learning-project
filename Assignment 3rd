import numpy as np
import pandas as pd

marks = np.array([
    [85,80,90],
    [70,75,65],
    [92,88,95],
    [60,72,68],
    [72,82,80],
]) 

# 1. Total marks per student
total_marks = np.sum(marks, axis=1)
print("Total marks obtained by each student:", total_marks)

# 2. Average marks per student
average_marks = np.mean(marks, axis=1)
print("Average marks of each student:", average_marks)

# 3. Average marks per subject
avg_subject = np.mean(marks, axis=0)
print("Average marks per subject:", avg_subject)

# 4. Highest score in each subject
highest = np.max(marks, axis=0)
print("Highest score in each subject:", highest)

# 5. Lowest score in each subject
lowest = np.min(marks, axis=0)
print("Lowest score in each subject:", lowest)

# 6. Students whose average marks are above 80
students_above_80 = np.where(average_marks > 80)[0]
print("Students with avg > 80:", students_above_80)

# 7. Pass/Fail status
pass_fail_status = np.where(average_marks >= 80, "Pass", "Fail")
print("Pass/Fail status:", pass_fail_status)

# 8. Index of highest-performing student
highest_performing = np.argmax(average_marks)
print("Highest performing student index:", highest_performing)

# 9. Standard deviation for each subject
stand_deviation = np.std(marks, axis=0)
print("Standard deviation per subject:", stand_deviation)

# 10. Variance for each subject
variance = np.var(marks, axis=0)
print("Variance per subject:", variance)

# Final DataFrame
frame = pd.DataFrame(
    marks, 
    columns=['Python', 'SQL', 'MachineLearning'], 
    index=['Student 1', 'Student 2', 'Student 3', 'Student 4', 'Student 5']
)

frame['Total Marks'] = total_marks
frame['Average Marks'] = average_marks
frame['Pass/Fail Status'] = pass_fail_status

print("\nFinal DataFrame:\n", frame.to_string())
