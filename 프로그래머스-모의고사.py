### 정답 풀이 ###
def solution(answers):
    # 패턴
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    # 출력값 
    ans_a = [a * (len(answers)//len(a)) + a[:len(answers)%len(a)] if len(a)<len(answers) else a[:len(answers)]][0]
    ans_b = [b * (len(answers)//len(b)) + b[:len(answers)%len(b)] if len(b)<len(answers) else b[:len(answers)]][0]
    ans_c = [c * (len(answers)//len(c)) + c[:len(answers)%len(c)] if len(c)<len(answers) else c[:len(answers)]][0]
    # 정답여부
    correct_a = len([ans_a[i] for i in range(len(answers)) if answers[i] == ans_a[i]])
    correct_b = len([ans_b[i] for i in range(len(answers)) if answers[i] == ans_b[i]])
    correct_c = len([ans_c[i] for i in range(len(answers)) if answers[i] == ans_c[i]])
    # 정답자
    ans = [correct_a, correct_b, correct_c]
    return [i+1 for i,v in enumerate(ans) if v == max(ans)]

### 틀린 풀이 ###
# 런타임 에러
# 하나씩 값을 비교하여 오랜 시간 소요됨
def solution(answers):
    answer = []
    # 패턴
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    # 출력값
    ans_a = [a * (len(answers)//len(a)) + a[:len(answers)%len(a)] if len(a)<len(answers) else a[:len(answers)]][0]
    ans_b = [b * (len(answers)//len(b)) + b[:len(answers)%len(b)] if len(b)<len(answers) else b[:len(answers)]][0]
    ans_c = [c * (len(answers)//len(c)) + c[:len(answers)%len(c)] if len(c)<len(answers) else c[:len(answers)]][0]
    # 정답여부
    correct_a = len([ans_a[i] for i in range(len(answers)) if answers[i] == ans_a[i]])
    correct_b = len([ans_b[i] for i in range(len(answers)) if answers[i] == ans_b[i]])
    correct_c = len([ans_c[i] for i in range(len(answers)) if answers[i] == ans_c[i]])
    # 정답자
    answer.append(1)
    if correct_a < correct_b:
        answer.remove(1)
        answer.append(2)
    elif correct_a == correct_b:
        answer.append(2)
    if max(correct_a, correct_b) < correct_c:
        answer.remove(max(correct_a, correct_b))
        answer.append(3)
    elif max(correct_a, correct_b) == correct_c:
        answer.append(3)
    return answer
