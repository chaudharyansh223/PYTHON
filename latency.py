response_times = {
    "auth_service": 120,
    "payment_gateway": 350,
    "user_profile": 120,
    "search_api": 410,
    "notification": 120
}
result = []
minimum_latency = min(response_times.values())
for service, latency in response_times.items():
    if latency == minimum_latency:
        result.append(service)
equivalent_latency = (minimum_latency,result)
print(equivalent_latency)


