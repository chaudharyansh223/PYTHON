raw_metrics = [
    "cpu:85",
    "mem:invalid",
    "disk:72",
    "network:",
    "gpu:90"
]
raw_dict_metrics = {}
for data in raw_metrics:
    left,right = data.split(":")
    try:
        raw_dict_metrics[left] = int(right)
    except Exception as e:
        print("some values doesn't convert in integer", e)
print(raw_dict_metrics)
