# import random
#
# N >=1 and N <=1000000
# num = random.randrange(-1000000, 1000001).split()
# numlist= []
#
# for i in range(1, N+1):
#     numlist.append[num]
#
# print(numlist)


# 여기

N = int(input())
number = [int(x) for x in input().split()]
mini = number[0]
maxi = number[0]

for i in range(1, len(number)):
    if maxi > number[i]:
        continue
    else:
        maxi = number[i]

for i in range(1, len(number)):
    if mini < number[i]:
        continue
    else:
        mini = number[i]

print(mini, maxi)




#input()함수 - 리스트 데이터를 입력할 때.
# a = [x for x in input("공백을 구분자로 데이터를 입력해보자: ").split()]
# print(a)
# print(type(a))
# a = [int(x) for x in input("공백을 구분자로 숫자를 입력바랍니다: ").split()]
# print(a)