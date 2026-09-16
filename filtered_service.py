servers = {
    "web1": "ubuntu",
    "db1": "centos",
    "web2": "ubuntu",
    "cache1": "debian",
    "db2": "centos"
}
same_os_service_grouped = {"ubuntu": [], "centos": [], "debian": []}
for service, os in servers.items():
    if os == "ubuntu":
        same_os_service_grouped["ubuntu"].append(service)
    elif os == "centos":
        same_os_service_grouped["centos"].append(service)
    else:
        same_os_service_grouped["debian"].append(service)
print(same_os_service_grouped)


