digit = int(input())
list = []
for i in range(digit):
    list.append(input())

for i in list:
    print(i)

print()

for i in list:
    if int(i[-1]) == 4 or int(i[-1]) == 5:
        print(i)