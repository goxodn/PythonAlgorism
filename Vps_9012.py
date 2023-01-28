n = int(input())

for i in range(n):
    vpsList = []
    error = 0

    userVps = input()
    for j in userVps:
        if j == '(':
            vpsList.append(j)
        elif j == ')':
            if len(vpsList) == 0:
                error = 1
                break
            else :
                vpsList.pop()

    if len(vpsList) == 0 and error == 0:
        print('YES')
    else :
        print('NO')