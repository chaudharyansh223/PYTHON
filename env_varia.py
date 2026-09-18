raw_env = [
    "APP_PORT=8080",
    "ENABLE_SSL=true",
    "TIMEOUT=30",
    "DEBUG=false",
    "APP_NAME=payments"
]
new_raw_env = {}
for items in raw_env:
    key, value = items.split("=")
    if value.isdigit():
        new_raw_env.update({key: int(value)})
    elif value.lower() == "true":
        new_raw_env.update({key: True})
    elif value.lower() == "false":
        new_raw_env.update({key: False})
    else:
        new_raw_env.update({key: value})
print(new_raw_env)

        


