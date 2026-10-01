server_a_packages = {"python", "nginx", "docker", "curl", "git"}
server_b_packages = {"docker", "git", "mysql", "redis", "python"}

only_in_a = []
only_in_b = []
common = []

if "python" in server_a_packages and "python" in server_b_packages:
    common.append("python")
if "nginx" in server_a_packages:
    only_in_a.append("nginx")
if "docker" in server_a_packages and "docker" in server_b_packages:
    common.append("docker")
if "curl" in server_a_packages:
    only_in_a.append("curl")
if "git" in server_a_packages and "git" in server_b_packages:
    common.append("git")
if "mysql" in server_b_packages:
    only_in_b.append("mysql")
if "redis" in server_b_packages:
    only_in_b.append("redis")

print("only_in_a:",only_in_a)
print("only_in_b:",only_in_b)
print("common:",common)