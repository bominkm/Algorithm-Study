## 정답 풀이 ##
import numpy as np

def isvalid(p):
    q = []

    p = np.array([list(x) for x in p])
    for y, x in zip(*np.where(p == 'P')):
        q.append((y, x, y, x, 0))    # (y, x, 시작'P'y, 시작'P'x, 거리)

    while q:
        y, x, sy, sx, d = q.pop(0)

        if d < 2:
            for ny, nx in [(y-1, x), (y, x+1), (y+1, x), (y, x-1)]: # 위, 오른쪽, 아래, 왼쪽
                if -1 < ny < 5 and -1 < nx < 5 and (ny, nx) != (sy, sx):
                    if p[ny, nx] == 'P': return 0
                    elif p[ny, nx] == 'O': q.append((ny, nx, sy, sx, d+1))

    return 1

def solution(places):
    return [isvalid(p) for p in places]
