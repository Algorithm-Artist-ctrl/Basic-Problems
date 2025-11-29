student = {"name": "Alice", "age": 20, "grade": "A"}

for key in student:
    print(key, ":", student[key])
    #or
for key, value in student.items():
    print(key, value)
