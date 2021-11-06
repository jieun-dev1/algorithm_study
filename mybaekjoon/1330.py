# A, B = input().split()
# A = int(A)
# B= int(B)
# 한줄로는 아래와 같다. map 함수 쓰면 3줄이 한 줄이 됨!

A, B = map(int, input().split())

A >=-10000
B <= 10000

def compare(A, B):
    if A>B:
        return('>')
    elif A<B:
        return('<')
    else:
        return('==')

print(compare(A, B))