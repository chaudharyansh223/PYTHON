scan_records = [
    {"ip": "192.168.1.1", "port": 80, "service": "HTTP"},
    {"ip": "192.168.1.2", "port": 443, "service": "HTTPS"},
    {"ip": "192.168.1.1", "port": 22, "service": "SSH"},
    {"ip": "192.168.1.3", "port": 22, "service": "SSH"},
    {"ip": "192.168.1.1", "port": 8080, "service": "HTTP-Proxy"},
    {"ip": "192.168.1.2", "port": 80, "service": "HTTP"}
]
group_port = {}
def group_ports(scan_records):
    for data in scan_records:
        ip = data["ip"]
        ports = data["port"]

        if ip not in group_port:
            group_port[ip] = []

        group_port[ip].append(ports)
    return group_port
print(group_ports(scan_records))



