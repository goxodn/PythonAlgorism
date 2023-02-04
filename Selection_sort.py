import random
#selection sort

def selection_sort(data):
    for i in range(len(data)-1):
        lowestNumber = i
        for j in range(i+1,len(data),1):
            if data[lowestNumber] > data[j] :
                lowestNumber = j
        data[i] , data[lowestNumber] = data[lowestNumber],data[i]

    return data

test_list = random.sample(range(100),10)

test_list = selection_sort(test_list)

for i in test_list:
    print(i ,end=' ')