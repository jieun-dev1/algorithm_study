#스터디 팀원 성호님 코드 - 원본: https://ooyoung.tistory.com/70
#알파벳 26글자를 전부 다 돌았던 내 코드보다 더 짧다 (set 으로 중복값을 제거했다)

words = input().upper()
unique_words = list(set(words)) # 입력받은 문자열에서 중복값 제거

cnt_list = []
for x in unique_words:
    cnt = words.count(x)
    cnt_list.append(cnt) #count 숫자를 list 에 append를 한다.

if cnt_list.count(max(cnt_list)) > 1:
    print('?')
else:
    max_index = cnt_list.index(max(cnt_list))
    print(unique_words[max_index])

