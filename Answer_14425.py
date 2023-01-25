a,b = map(int,input().split())

wordList = []
mList = []
count = 0

for i in range(a+b):
    if i < a :
        wordList.append(input())
    else:
        mList.append(input())

for i in wordList :
    for j in mList :
        if i == j :
            count = count + 1
print(count)