num = int(input())

xyList = []

for i in range(num):
    [x,y] = map(int, input().split())
    reverse = [y,x]
    xyList.append(reverse)

xyList = sorted(xyList,reverse=False)

for i in range(len(xyList)):
    print(xyList[i][1],xyList[i][0])