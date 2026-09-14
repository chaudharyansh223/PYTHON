status_codes = ["200", "200", "500", "404", "200", "503", "301", "200"]
response = {"total_request": 0, "total_error": 0, "error_percentage": 0}
for reponse in status_codes:
    if reponse.startswith("5") or reponse.startswith("4"):
        response["total_error"]+=1
    else:
        response["total_request"]+=1
response["error_percentage"] = round((response["total_request"] / response["total_error"])*100,1) 
print(response)