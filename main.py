import pandas as pd

data = pd.read_csv("student_data.csv")
data_score = data["Score"]

number_of_student = len(data_score)
list_of_score = data_score.to_list()

mean_score = data_score.mean()
median_score = data_score.median()
mode_score = data_score.mode().tolist()
max_score = data_score.max()
min_score = data_score.min()
standard = data_score.std()

passed_student = (data_score >= 50).sum()
failed_student = (data_score < 50).sum()

print("Total Students:", number_of_student)
print("Mean Score:", mean_score)
print("Median Score:", median_score)
print("Mode Score(s):", ", ".join(map(str, mode_score)))
print("Max Score:", max_score)
print("Min Score:", min_score)
print("Standard Deviation:", standard)
print("Passed Students:", passed_student)
print("Failed Students:", failed_student)
