import random
# insertion Sort

def insertion_sort(data):
    for i in range(len(data) - 1):
        for j in range(i, 0, -1):
            if data[j - 1] > data[j]:
                data[j - 1], data[j] = data[j], data[j - 1]
            else:
                break
    return data

data_list = random.sample(range(100),10)

data_list = insertion_sort(data_list)

for i in data_list:
    print(i ,end =' ')