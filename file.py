scores = {
    "Alice": 78,
    "Bob": 92,
    "Charlie": 65,
    "David": 92,
    "Eve": 84
}
filtered_student = []
topper_student = ()
marks = max(scores.items(), key=lambda x: x[1])
for key, value in scores.items():
    if marks[1] == value:
        filtered_student.append(key)
topper_student = (marks[1],filtered_student)     
print(topper_student)


        
