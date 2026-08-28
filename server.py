ping_data = [
    "server1: 45ms",
    "server2: 120ms",
    "server3: 85ms",
    "server4: 210ms",
    "server5: 95ms"
]
new_value = ""
average_latency = 0
def get_data():
    sum = 0
    for data in ping_data:
        key, value = data.split(": ")
        new_value = value.replace("ms","")
        sum+=int(new_value)
    average_latency = round(sum / len(ping_data), 2)

    return average_latency
def filtering_server(average_latency):
    filtered_server = []
    for data in ping_data:
        key, value = data.split(": ")
        new_value = value.replace("ms","").strip()
        if int(new_value) > average_latency:
            filtered_server.append(key)
    print("average latency of server:", average_latency)
    print("servers whose latency is above than average latency:",filtered_server)
def main():
    avg_latency = get_data()
    filtering_server(avg_latency)
if __name__ == "__main__":
    main()


            