while True:
    word = input()
    if word == '.':
        break
    vpsList = []
    error = 0
    for i in word:
        if i == '(' or i == '[':
            vpsList.append(i)
        if i == ')' or i == ']' :
            if len(vpsList) != 0 :
                data = vpsList.pop()
            else :
                error = error + 1
                break
            if data == '(' and i == ')':
                continue
            elif data == '[' and i == ']':
                continue
            else :
                error = 1
    if len(vpsList) == 0 and error == 0:
        print('yes')
    else :
        print('no')

