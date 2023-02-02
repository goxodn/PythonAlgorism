import random


def mergesplit(data):
    if len(data) <= 1:
        return data
    else:
        midium = int(len(data) / 2)
        left = mergesplit(data[:midium])
        right = mergesplit(data[midium:])
    return merge(left, right)


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

data_list = random.sample(range(100), 10)
for i in mergesplit(data_list):
    print(i, end=' ')
