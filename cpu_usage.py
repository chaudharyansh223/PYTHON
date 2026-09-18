containers = [
    {"name": "api_gateway", "status": "running", "cpu_usage": 45.5},
    {"name": "auth_service", "status": "running", "cpu_usage": 88.2},
    {"name": "db_migrator", "status": "stopped", "cpu_usage": 95.0},
    {"name": "worker_queue", "status": "running", "cpu_usage": 80.0},
    {"name": "cache_layer", "status": "running", "cpu_usage": 72.1}
]
filtered_list = []
for data in containers:
    if data["status"] == "running" and data["cpu_usage"] >= float(80):
        filtered_list.append(data["name"])
print(filtered_list)


