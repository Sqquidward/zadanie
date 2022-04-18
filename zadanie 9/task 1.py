digit = int(input())
list = []
for i in range(digit):
    list.append(int(input()))
count = int(input())
flag = True
for i in range(len(list)):
    for j in range(len(list)):
        if list[i] * list[j] == count and i != j:
            flag = False
        break

if flag == True:
    print('no')
else:
    print('ок')