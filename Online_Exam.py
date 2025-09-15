def check_pass_fail(marks):
    num_subjects = len(marks)
    if any(mark < 40 for mark in marks):
        return "Fail"
    average = sum(marks) / num_subjects
    if average >= 50:
        return "Pass"
    else:
        return "Fail"
subjects = ["Math", "Science", "English", "History"]
marks = []
for subject in subjects:
    score = float(input(f"Enter marks for {subject}: "))
    marks.append(score)
result = check_pass_fail(marks)
print(f"\nResult: {result}")
