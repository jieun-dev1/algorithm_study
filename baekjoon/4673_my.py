#영지공지님 블로그 참조.

#문제:10000보다 작거나 같은 셀프 넘버를 (생성자가 없는수) 한 줄에 하나씩 출력하기.
#생성자 리스트를 먼저 찾고, 1부터 10,000 까지 리스트에서 생성자 리스트를 뺴기.
#생성자란? 양의 정수 n에 대해서 d(n)을 n과 n의 각자리수를 더하는 함수라고 할 때. d(75) = 75+7+5, 즉 82이다.
#n을 d(n)의 생성자라고 한다. 그래서 75는 82의 생성자이다.
#전체 1-10000 리스트 중 생성자가 있는 수를 제외해서 셀프 넘버 리스트를 만든다.

numbers = list(range(1, 10001))
remove_list = []
for num in numbers:
    for n in str(num):
        num += int(n) #num 은 생성자가 있는 숫자이다.
    if num <=10000:
        remove_list.append(num)
for remove_num in set(remove_list): #101의 생성자는 91과  100이다. 이렇듯 생성자가 생성자가 2개 있을 경우를 대비해서 set 으로 중복 제거
    numbers.remove(remove_num)
for self_num in numbers: #이제 생성자가 있는 숫자가 삭제되었으니 남은 것은 self_num 이다.
    print(self_num)
