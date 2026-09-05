raw_list = [4, 5, 2, 4, 1, 5, 9, 2, 3]
current_idx_4 = 0
current_idx_5 = 1
filtered_list = []
for current_idx, num in enumerate(raw_list):
    if current_idx == current_idx_4 or current_idx == current_idx_5:
        filtered_list.append(num)
        continue
    if num not in filtered_list:
        filtered_list.append(num)    
print(filtered_list) 