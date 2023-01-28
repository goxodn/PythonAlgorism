n = int(input())
z = []
for i in range(n):
    num = int(input())
    if num == 0:
        z.pop()
    else:
        z.append(num)
print(sum(z))

# stack_list = []
# count = 0
#
# def push(data):
#     stack_list.append(data)
#
# def pop():
#     data = stack_list[-1]
#     del stack_list[-1]
#     return data
#
# K = int(input())
#
# for i in range(K):
#     data = int(input())
#     if data != 0 :
#         push(data)
#     else :
#         pop()
#
# print(sum(stack_list))