log_messages = [
    "ERR_01: Network connection drop",
    "INFO_02: Cache cleared successfully",
    "ERR_03: Disk read fail",
    "WARN_01: High memory alert",
    "ERR_04: CPU temperature spike"
]
new_data = []
for line in log_messages:
    if line.startswith("ERR"):
        new_line =  line.upper().split(": ")[1]
        new_data.append(new_line)
print(new_data)
