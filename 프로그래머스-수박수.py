def solution(n):
    word = '수박'
    return word*(n//2)+word[0]*(n%2)
