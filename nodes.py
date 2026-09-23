class Servercluster:
    def __init__(self):
        self.node = {}

    def add_node(self, hostname,memory_gb):
        if hostname in self.node:
            return f"node {hostname} is already exist"
        else:
            self.node[hostname] = memory_gb
            return f"node {hostname} added"
    def get_total_memory(self):
        sum = 0
        for value in self.node.values():
            sum+= value
        return int(sum)
    def remove_node(self, hostname):
        if hostname in self.node:
            self.node.popitem()
            return f"node {hostname} removed"
        else:
            print(f"node {hostname} isn't exist")
            self.add_node(hostname, 33)
            print(f"node {hostname} added")
            return f"available nodes are: {self.node}"




cluster_name = Servercluster()
print(cluster_name.add_node("node-1", 16))
print(cluster_name.add_node("node-2", 32))
print(cluster_name.get_total_memory())
print(cluster_name.remove_node("node-1"))
print(cluster_name.remove_node("node-3"))