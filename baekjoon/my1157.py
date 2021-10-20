#제출 시 주석처리
string = "zZa"

# 1. 대소문자 구별 없으니 그냥 upper 를 해준다.
# 2. 알파벳을 ASCII 코드로 바꿔서(ord 사용).
# 3. 숫자를 인덱스 값으로 하고, OCCURENCE 를 세준다.
# 4. if 문을 돌리면서, max_alphabet 과 alphabet_occurence 를 갱신해준다.
# * 27줄에서 indentation 을 하지 않아서, 답이 오류가 났었다. 여기서 indentation 하면 if else 가 같이 for문을 돌기 때문에 꼭 들여쓰기 해줘야 함.
# * 맨 앞에 string = input().upper() 하고 input 을 정의해주니까 런타임에러(name에러가 나지 않는다)

string = input().upper()
def find_max_occurred_alphabet(string):
    alphabet_occurrence_array = [0] * 26
    for char in string:
        arr_index = ord(char) - ord("A")
        alphabet_occurrence_array[arr_index] += 1

    max_occurrence = 0
    max_alphabet_index = 0

    for index in range(len(alphabet_occurrence_array)):
        alphabet_occurrence = alphabet_occurrence_array[index]

        if alphabet_occurrence > max_occurrence:
            max_occurrence = alphabet_occurrence
            max_alphabet_index = index

    if alphabet_occurrence_array.count(max_occurrence) >= 2:
        return print('?')

    else:
        return print(chr(max_alphabet_index + ord("A")))

result = find_max_occurred_alphabet(string)
# print(result)
