## 정답 풀이 ##
# 2차원 좌표로 생각
# num: 눌러야할 번호
# hands: 현재 손가락 위치
# answer: 누른 손가락
# hand: 오른손잡이 or 왼손잡이
def click(num, hands, answer, hand):
    # 키패드별 좌표
    tel = {'*':[0,0], '#':[2,0], 0:[1,0], 1:[0,3], 2:[1,3], 3:[2,3], 4:[0,2], 5:[1,2], 6:[2,2], 7:[0,1], 8:[1,1], 9:[2,1]}
    if num in [1,4,7]:
        hands[0] = tel[num]
        answer.append('L')
    elif num in [3,6,9]:
        hands[1] = tel[num]
        answer.append('R')
    else:
        # 거리계산
        left = abs(hands[0][0]-tel[num][0])+abs(hands[0][1]-tel[num][1])
        right = abs(hands[1][0]-tel[num][0])+abs(hands[1][1]-tel[num][1])
        if left > right:
            hands[1] = tel[num]
            answer.append('R')
        elif left < right:
            hands[0] = tel[num]
            answer.append('L')
        else:
            if hand == 'right':
                hands[1] = tel[num]
                answer.append('R')
            else:
                hands[0] = tel[num]
                answer.append('L')
    return hands, answer
  
  def solution(numbers, hand):
    move = [[0,0],[2,0]]; answers = []
    for nums in numbers:
        move,answers = click(nums, move, answers, hand)
    return ''.join(answers)
