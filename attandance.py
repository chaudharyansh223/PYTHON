attendance_records = {
    "Amit": [1, 1, 1, 0, 1],
    "Pooja": [1, 1, 1, 1, 1],
    "Ravi": [0, 1, 0, 1, 0],
    "Sneha": [1, 0, 1, 0, 1]
}
attandance = {"total_present_amit": 0, "total_present_pooja": 0, "total_present_ravi": 0, "total_present_sneha": 0}
attandance_status = {"eligible": [], "debared": []}
for student, present in attendance_records.items():
    for days in present:
        if student == "Amit":
            attandance["total_present_amit"]+= days
        elif student == "Pooja":
            attandance["total_present_pooja"]+= days
        elif student == "Ravi":
            attandance["total_present_ravi"]+= days
        else:
            attandance["total_present_sneha"]+= days


present_percentage_amit = (attandance["total_present_amit"] / len(attendance_records["Amit"]))*100
present_percentage_pooja = (attandance["total_present_pooja"] / len(attendance_records["Pooja"]))*100
present_percentage_ravi = (attandance["total_present_ravi"] / len(attendance_records["Ravi"]))*100
present_percentage_sneha = (attandance["total_present_sneha"] / len(attendance_records["Sneha"]))*100
for name, available in attendance_records.items():
    if name == "Amit":
        if present_percentage_amit >= float(75):
            attandance_status["eligible"].append(name)
        else:
            attandance_status["debared"].append(name)
    elif name == "Pooja":
        if present_percentage_pooja >= float(75):
            attandance_status["eligible"].append(name)
        else:
            attandance_status["debared"].append(name)
    elif name == "Ravi":
        if present_percentage_ravi >= float(75):
            attandance_status["eligible"].append(name)
        else:
            attandance_status["debared"].append(name)
    elif name == "Sneha":
        if present_percentage_sneha >= float(75):
            attandance_status["eligible"].append(name)
        else:
            attandance_status["debared"].append(name)
print(attandance_status)
    






