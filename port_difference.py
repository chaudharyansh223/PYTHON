node_a_ports = [22, 80, 443, 8080, 9000]
node_b_ports = [80, 443, 3306, 5432, 9000]
port_a_set = set(node_a_ports)
port_b_set = set(node_b_ports)
port_difference = port_a_set ^ port_b_set
sort_accending = sorted(port_difference)
print(sort_accending) 
