# 엘리스씨는 가장 적은 힘을 사용하여 주어진 모든 점토를 합치고 싶어졌습니다.
# 엘리스씨를 도와 n개의 점토를 하나의 덩이로 합치기 위해 필요한 힘의 크기의 합의 최솟값을 구하는 프로그램을 작성하세요.

'''
4
1 5 7 3
'''
import heapq

import heapq

def getMinForce(weights):
    '''
    n개의 점토를 하나로 합치기 위해 필요한 힘의 합의 최솟값을 반환하는 함수
    '''
    heapq.heapify(weights)  # weights를 최소 힙으로 변환
    result = 0

    while len(weights) > 1:
        # 가장 가벼운 두 개를 꺼내서 합친다
        x = heapq.heappop(weights)
        y = heapq.heappop(weights)
        force = x + y
        result += force
        heapq.heappush(weights, force)  # 합친 점토를 다시 넣음

    return result

n = int(input())
weights = list(map(int, input().split()))

print(getMinForce(weights))