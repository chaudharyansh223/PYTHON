processes = [
    {"pid": 1042, "name": "python", "mem_mb": 512},
    {"pid": 2105, "name": "chrome", "mem_mb": 1400},
    {"pid": 3312, "name": "code", "mem_mb": 850},
    {"pid": 4519, "name": "slack", "mem_mb": 1100}
]
filtered_pis = {"kill_pids": [], "reclaimed_mb": 0}
restored_mb = 0
for data in processes:
    if data["mem_mb"] > 1000:
        filtered_pis["kill_pids"].append(data["pid"])
        restored_mb+= data["mem_mb"]
filtered_pis["reclaimed_mb"]+= int(restored_mb)
print(filtered_pis)
        
