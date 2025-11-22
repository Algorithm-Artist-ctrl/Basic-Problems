student = {
    "name": "Alex",
    "age": 20,
    "grade": "A"
}

student["age"] = 21                         
student["major"] = "Computer Science"       

for key, value in student.items():          
    print(key, ":", value)
