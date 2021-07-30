### 정답 풀이 ###
import re; from itertools import permutations
# 각 연산자에 따른 계산값 출력함수 
def calculate(chr_n, chr_m, operator):
    idx_m = [i for i,v in enumerate(chr_m) if v == operator]
    j = 0
    for i in idx_m:
        chr_n[i-j] = eval(''.join([str(chr_n[i-j])] + [chr_m[i-j]] + [str(chr_n[i+1-j])]))
        del chr_n[i+1-j]
        chr_m.remove(chr_m[i-j])
        j += 1
    return chr_n, chr_m
def solution(expression):
    # 숫자와 수식 구분
    answer = []; nums = []; maths = []
    nums.extend(re.findall('\d+', expression))
    maths.extend(re.findall('\D', expression))
    # 우선순위 조합
    for case in list(permutations(set(maths), len(set(maths)))):
        chr_n = nums[:]; chr_m = maths[:]
        # 각 수식에 따른 계산값 출력
        for i in range(len(case)):
            chr_n, chr_m = calculate(chr_n, chr_m, case[i])
        answer.append(abs(chr_n[0]))
    return max(answer)

### 틀린 풀이 ###
import re; from itertools import permutations
# 각 연산자에 따른 계산값 출력함수 
# chr_n: 숫자 리스트
# chr_m: 연산자 리스트
# math: 부호
def calculate(chr_n, chr_m, math):
    if math in chr_m:
        idx_m = [i for i,v in enumerate(chr_m) if v == math]
        if math == '-':
            cal = [float(chr_n[v])-float(chr_n[v+1]) for v in idx_m]
        elif math == '+':
            cal = [float(chr_n[v])+float(chr_n[v+1]) for v in idx_m]
        else:
            cal = [float(chr_n[v])*float(chr_n[v+1]) for v in idx_m]
        j = 0
        for i in range(len(idx_m)):
            chr_n[idx_m[i]-j] = cal[i]
            del chr_n[idx_m[i]+1-j]
            j += 1
            chr_m.remove(math)
    return chr_n, chr_m
def solution(expression):
    # 숫자와 수식 구분
    answer = []; nums = []; maths = []
    nums.extend(re.findall('\d+', expression))
    maths.extend(re.findall('\D', expression))
    iter_num = nums; iter_maths = maths
    # 우선순위 조합
    for case in list(permutations(set(maths), len(set(maths)))):
        # 각 수식에 따른 계산값 출력
        for i in range(len(case)):
            iter_num, iter_maths = calculate(iter_num, iter_maths, case[i])
        answer.append(abs(iter_num[0]))
    return int(max(answer))
