## 정답 풀이 ##
def bfs(begin, target, words, visited):
    count = 0
    stack = list()
    stack.append(begin)

    while stack:
        current_word = stack.pop()
        
        # target 단어인 경우
        current_word = stack.pop()
        if current_word == target:
            return count

        for i in range(len(words)):
            # 방문한 적 있는지 확인
            if visited[i] == True:
                continue
            
            # 차이나는 문자 수 세기
            cnt = 0
            for a,b in zip(current_word, words[i]): 
                if a != b:
                    cnt += 1
                    
            # 한글자만 차이나면 방문
            if cnt == 1:
                visited[i] = True
                stack.append(words[i])

        count += 1

    return count


def solution(begin, target, words):
    answer = 0
    visited = [False] * len(words)
    return bfs(begin, target, words, visited)
