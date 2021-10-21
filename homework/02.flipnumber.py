input = "011110"

#주어진 문자열을 모두 0 혹은 모두 1로 같게 만드는 최소 횟수를 반환하시오.

#011110
#모두 0으로 만드는 방법에서 최소로 뒤집는 숫자.
# count_to_all_zero
#0에서 1로 전환되는 순간, count_to_all_zero += 1

#모두 1로 만드는 방법에서 최소로 뒤집는 순간.
# count_to_all_one
# 1 -> 0 으로 문자열이 전환되는 순간 count_to_all_one += 1

#1) 뒤집어질 때, 즉 0에서 1 혹은 1에서 0으로 바뀔 때.
#2) 첫 번째 원소가 0인지 1인지에 따라서 숫자를 추가해줘야 함.

def find_count_to_turn_out_to_all_zero_or_all_one(string):
    count_to_all_zero = 0
    count_to_all_one = 0

    if string[0] == '0':
        count_to_all_one +=1

    elif string[0] == '1':
        count_to_all_zero += 1

    for i in range(len(string) - 1):
        if string[i] != string[i+1]: #1이면 0으로 가고, 0이면 1로 가는.
            if string[i+1] == '0':
                count_to_all_one += 1
            if string[i+1] == '1':
                count_to_all_zero += 1
    return min(count_to_all_one, count_to_all_zero)


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)