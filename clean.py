query = "user=ansh&role=admin&env=prod&debug=true"
new_query = query.split("&")
modified = {}
for data in new_query:
    key, value = data.split("=")
    modified.update({key: value})
print(modified)



