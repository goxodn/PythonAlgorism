## 대표적인 정렬 : 퀵 정렬

## 퀵 정렬 이란 ?

## 정렬 알고리즘의 꽃
## 기준점(pivot 이라고 부름)을 정해서 기준점보다 작은 데이터는 왼쪽 큰 데이터는 오른쪽으로 모으는 함수를 작성함
## 함수는 왼쪽 + 기준점 + 오른쪽을 리턴함

## 3 2 5 4 1

def qsort(data):
    if len(data) <= 1:
        return data
    ## 5

    left,right = list(),list()
    pivot = data[0]

    ## left [] right []
    ## pivot = 3


    for index in range(1,len(data)):
        ##1,5 1,2,3,4 0을 안하는 이유는 pivot을 0으로 정했기 때문
        if pivot > data[index]:
            ## data[1] = 2 pivot = 3 더 작기 때문에 left로
            left.append(data[index])
            ##left = [2,1]
        else :
            right.append(data[index])
            ##right = [5,4]
    return qsort(left) + [pivot] + qsort(right)

    ## qsort([2,1]) + [3] + qsort((5,4))

    ## qsort(left)

    ## pivot = 2

    ## left = 1

    ## qsort(1) + 2

    ## 1 + 2

    ## qsort((2,1)) == [1,2] -> + [3] + qsort(4,5)