n = int(input())
list = ['']*n
for i in range(n):
    list[i] = input()

k = int(input())
for i in range(k):
    x = int(input())
    digit = ['']*x
    for j in range(x):
        digit[j] = list[int(input())-1]
    list = digit

for i in range(len(list)):
    print(list[i])