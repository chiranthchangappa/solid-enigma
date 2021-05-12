list_entry = [5, 6, 3, 4, 2, 1]

for i in range(len(list_entry)): # 5
    for j in range(len(list_entry) -i-1) :
        if list_entry[j] > list_entry[j+1]:
            list_entry[j], list_entry[j+1] = list_entry[j+1], list_entry[j]

print(list_entry)