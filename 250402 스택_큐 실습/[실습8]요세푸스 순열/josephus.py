'''
josephus_sequence 함수를 작성하세요.
'''
from collections import deque


def josephus_sequence(n, k) :
    dq = deque(range(1,n+1))

    answer = []

    while len(answer) < n:
        for i in range(k - 1):
            dq.append(dq.popleft())
        answer.append(dq.popleft())

    return answer