import random
#
def merge_split(data):
    if len(data) <= 1 :
        return data
    medium = int(len(data)/2)
    left = merge_split(data[:medium])
    right = merge_split(data[medium:])
    return merge(left,right)

def merge(left, right):
    merged = list()
    left_point, right_point = 0, 0

    # case 1 : left/right가 아직 남아있을때
    while len(left) > left_point and len(right) > right_point:
        if left[left_point] > right[right_point]:
            merged.append(right[right_point])
            right_point += 1
        else:
            merged.append(left[left_point])
            left_point += 1

            # case 2 : left만 남아있을때
    while len(left) > left_point:
        merged.append(left[left_point])
        left_point += 1

        # case 3 : right만 남아있을때
    while len(right) > right_point:
        merged.append(right[right_point])
        right_point += 1

    return merged





#Quick Sort
def quick_sort(data):
    if len(data) <= 1:
        return data

    left,right = list(),list()
    pivot = data[0]

    for index in range(1,len(data)):
        if pivot > data[index]:
            left.append(data[index])
        else :
            right.append(data[index])
    return quick_sort(left) + [pivot] + quick_sort(right)

#36 48 61 75 3 5 1 2 81 87 91 98
# 36


def bubble_sort(data):
    #7
    for index in range(len(data)-1):
        for j in range(len(data)-index-1):
            if data[j] > data[j+1] :
                data[j],data[j+1] = data[j+1],data[j]

    return data

def insertion_sort(data):
    for i in range(len(data) - 1):
        for j in range(i, 0, -1):
            if data[j - 1] > data[j]:
                data[j - 1], data[j] = data[j], data[j - 1]
            else:
                break
    return data


def selection_sort(data):
    for i in range(len(data)-1):
        lowestNumber = i
        for j in range(i+1,len(data),1):
            if data[lowestNumber] > data[j] :
                lowestNumber = j
        data[i] , data[lowestNumber] = data[lowestNumber],data[i]

    return data

test_list = random.sample(range(100),20)

test_list = selection_sort(test_list)

for i in test_list:
    print(i,end=' ')

