incoming_requests = ["10.0.0.1", "192.168.1.100", "172.16.0.5", "10.0.0.1", "192.168.1.100"]
blocked_ips = {"192.168.1.100", "192.168.1.101"}
filtered_duplicate_ip = set()
result = {"allowed": [], "blocked_ip": []}
def duplicate_ip(incoming_requests):
    for ip in incoming_requests:
        if ip not in filtered_duplicate_ip:
            filtered_duplicate_ip.add(ip)

    return filtered_duplicate_ip
def check_blocked_ip(filtered_duplicate_ip):
    for ip in filtered_duplicate_ip:
        if ip in blocked_ips:
            result["blocked_ip"].append(ip)
        else:
            result["allowed"].append(ip)
    print(result)

def main():
    duplicate_ip(incoming_requests)
    check_blocked_ip(filtered_duplicate_ip)
main()
    
