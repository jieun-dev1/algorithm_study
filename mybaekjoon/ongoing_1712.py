#정답

A, B, C = map(int, input().split())
if B>C:
    print(-1)
elif B==C:
    print(-1)
else:
    print(int(A/(C-B)+1))

# A, B, C = input().split() -> 얘가 안되는 이유 -> int 가 안되기 떄문.. 그러니 map함수 쓰자.
#(1) 실수. B>=C 해주면, 0인 경우 0으로 나눌 때 에러가 생긴다. 이때도 -1처리를 따로 해주자.
#(2) 아래처럼 하면 안되는 이유.
#i=0일 때나, 0보다 작을 떄의 예외처리를 해줘야 함..(continue 는 적용 안됨) 여기서 반대로 해주면 더 쉬움.
#C-B 가 0보다 큰 한, i는 항상 존재할 수 밖에 없다.

# A, B, C = map(int, input().split())
# i = int(A/(C-B))
# if (C-B)<=0:
#     print("-1")
# else:
#     if i > 0:
#         print(i+1)





