services = [
    "nginx:running",
    "mysql:stopped",
    "redis:running",
    "docker:stopped",
    "cron:running"
]
service_status = {"active": 0, "inactive": 0, "inactive_services": [] }
for record in services:
    service_name, status = record.split(":")
    if status == "running":
        service_status["active"] = service_status.get("active", 0)+1
    if status == "stopped":
        service_status["inactive"] = service_status.get("inactive", 0)+1
        service_status["inactive_services"].append(service_name)
       
print(service_status)




