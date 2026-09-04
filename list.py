auth_logs = [
    "Failed password for root from 192.168.1.5 port 22 ssh2",
    "Accepted password for user1 from 192.168.1.10 port 22 ssh2",
    "Failed password for admin from 192.168.1.5 port 22 ssh2",
    "Failed password for root from 10.0.0.1 port 22 ssh2",
    "Failed password for test from 192.168.1.5 port 22 ssh2"
]
failed_attempts = {"192.168.1.5": 0, "10.0.0.1": 0}
for record in auth_logs:
    if record.startswith("Failed"):
        if "192.168.1.5" in record:
            failed_attempts["192.168.1.5"]+=1
        if "10.0.0.1" in record:
            failed_attempts["10.0.0.1"]+=1
filtered_failed_attempts = {}
for key, value in failed_attempts.items():
    if value > 2:
        filtered_failed_attempts.update({key: value})
print(filtered_failed_attempts)

