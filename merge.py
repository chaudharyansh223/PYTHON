cluster_a = {"frontend": 120, "backend": 450, "auth": 80}
cluster_b = {"backend": 300, "database": 600, "frontend": 80}
new_clusterab = {}
new_clusterab = cluster_b.copy()
if "frontend" in new_clusterab:
    new_clusterab["frontend"]+= cluster_a["frontend"]
if "backend" in new_clusterab:
    new_clusterab["backend"]+= cluster_a["backend"]
new_clusterab.update(cluster_a)
print(new_clusterab)

