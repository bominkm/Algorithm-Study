## 정답 풀이 ##
def solution(record):
    # key: 유저 아이디, value: 닉네임
    names = {}; answer = []
    for records in record:
        if records.split(' ')[0] == 'Enter':
            names[records.split(' ')[1]] = records.split(' ')[2]
            answer.append([records.split(' ')[1], '님이 들어왔습니다.'])
        elif records.split(' ')[0] == 'Leave':
            answer.append([records.split(' ')[1], '님이 나갔습니다.'])
        else:
            names[records.split(' ')[1]] = records.split(' ')[2]
    for i in range(len(answer)):
        # 유저 아이디 -> 닉네임
        answer[i][0] = names[answer[i][0]]
        answer[i] = ''.join(answer[i])
    return answer
