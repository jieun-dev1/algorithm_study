#우성호님 코드

def d(num):
    return num + sum(map(int, str(num)))

num_list = []

for i in range(1,10001):
    num_list.append(d(i))

for i in range(1,10001):
    if i not in num_list:
        print(i)