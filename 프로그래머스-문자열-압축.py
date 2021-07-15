### 정답 풀이 ###
def solution(text):   
    length = []
    length.append(len(text))
    # 자르는 단위
    for i in range(1, len(text)//2+1):
        num = [len(text)//i + 1 if len(text)%i != 0 else len(text)//i][0]
        # 반복되는지
        words = []
        for word in [text[j*i:(j+1)*i] for j in range(num)]:
            if len(words) == 0:
                words.append(str(1))
                words.append(word)
                continue
            if words[-1] != word:
                words.append(str(1))
                words.append(word)
            else:
                words[-2] = str(int(words[-2]) + 1)
        # 문자열 만들기
        while '1' in words: words.remove(str(1))
        length.append(len(''.join(words)))
    return min(length)

### 틀린 풀이 ###
# 직전의 값이 같아야 압축된다는 점을 놓침
def solution(text):   
    length = []
    length.append(len(text))
    # 자르는 단위
    for i in range(1, len(text)//2+1):
        num = [len(text)//i + 1 if len(text)%i != 0 else len(text)//i][0]
        # 반복되는지
        words = {}
        for word in [text[j*i:(j+1)*i] for j in range(num)]:
            if word not in words:
                words[word] = 1
            else:
                words[word] += 1
        # 문자열 만들기
        make = []
        for k in range(len(words)):
            if list(words.values())[k] != 1:
                make.append(str(list(words.values())[k]))
            make.append(list(words.keys())[k])
        length.append(len(''.join(make)))
    return min(length)
