import sys

def mergeSplit(data):
    if len(data) <= 1 :
        return data
    medium = int(len(data)/2)
    left = mergeSplit(data[:medium])
    right = mergeSplit(data[medium:])
    return merge(left,right)

def merge(left,right):
    merged = list()
    left_index,right_index = 0,0

    #case 1 left,right 둘 다 사이즈가 0이 아닐때
    while len(left) > left_index and len(right) > right_index:
        if left[left_index] > right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        else :
            merged.append(left[left_index])
            left_index += 1

    #case 2 left 리스트 사이즈가 0일경우
    while len(right) > right_index :
        merged.append(right[right_index])
        right_index += 1

    #case 3 right 리스트 사이즈가 0일 경우
    while len(left) > left_index :
        merged.append(left[left_index])
        left_index += 1

    return merged

N = int(sys.stdin.readline())

numList = []
for index in range(N):
    numList.append(int(sys.stdin.readline()))

for i in mergeSplit(numList):
    print(i)

