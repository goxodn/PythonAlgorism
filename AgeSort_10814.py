n = int(input())
list = []

for i in range(n):
    age,name = input().split()
    age = int(age)
    list.append([age,name,i])

list.sort(key=lambda x:(x[0],x[2]))

for i in list:
    print(i[0],i[1])