### 정답 풀이 ###
# 문제 조건 꼼꼼히 확인하여 조건문 빠뜨리지 않기
def solution(new_id):
    new_id = new_id.lower()
    new_id = ''.join([new_id[i] if (new_id[i].isalpha()) | (new_id[i].isdigit()) | (new_id[i] == "-") | (new_id[i] == "_") | (new_id[i] == ".") else '' for i in range(len(new_id))])
    list3 = list(new_id[0]) + ['' if (new_id[i] == ".") & (new_id[i-1] == ".") else new_id[i] for i in range(1,len(new_id))]
    new_id = ''.join(list3)
    list4 = list(new_id)
    if len(list4) > 0:
        if list4[0] == '.': list4.remove('.')
    if len(list4) > 0:
        if list4[-1] == '.': list4 = list4[:-1]
    new_id = ''.join(list4)
    if len(new_id) == 0: new_id = "a"
    if len(new_id) >= 16: new_id = ''.join(list(new_id)[:15])
    if new_id[-1] == '.': new_id = new_id[:-1]
    if len(new_id) <= 2: new_id = new_id + (3-len(new_id))*new_id[-1]
    return new_id
