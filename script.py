raw_config = [
    "# Application Configuration",
    "PORT=8080",
    "",
    "  HOST=127.0.0.1  ",
    "# Database Settings",
    "DB_NAME=production_db",
    "   ",
    "DEBUG=False",
    "# End of file"
]
modified_records = {}
for record in raw_config:
    cleaned = record.strip()
    if not cleaned or cleaned.startswith("#"):
        continue
    key, value = cleaned.split("=")
    modified_records.update({key: value})
print(modified_records)