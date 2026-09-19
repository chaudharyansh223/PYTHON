raw_ports = ["80", "443", "twenty-two", "8080", "invalid", "3306", "None"]
parse_port_list = {"valid_ports": [], "failed_values": []}
def parse_port(raw_ports):
    for ports in raw_ports:
        try:
        
                parse_port_list["valid_ports"].append(int(ports))
        except:
            parse_port_list["failed_values"].append(ports)
    return parse_port_list
print(parse_port(raw_ports))