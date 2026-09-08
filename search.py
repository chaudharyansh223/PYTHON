disks = [
    {"filesystem": "/dev/sda1", "total_gb": 100, "used_gb": 85},
    {"filesystem": "/dev/sda2", "total_gb": 500, "used_gb": 200},
    {"filesystem": "/dev/sdb1", "total_gb": 50, "used_gb": 48}
]
filtered_data = []
for data in disks:
    percentage = (data["used_gb"] / data["total_gb"])*100
    if percentage > 80:
        filtered_data.append(({"filesystem": data["filesystem"], "usage_percentage": round(percentage,1)}))
print(filtered_data)
