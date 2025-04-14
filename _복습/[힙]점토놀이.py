# 점토놀이
# n개의 점토를 하나의 덩이로 합치기 위해 필요한 힘의 크기의 합의 최소값을 구하는 프로그램을 작성하자
import heapq
# 입력값 : 1 5 7 3
# 출력값 : 29
# 즉, 최소로 정렬하고 합치는 거임


def getMinForce(weights):
    heapq.heapify(weights) #최소힙

    result = 0

    while len(weights) > 1:
        x = heapq.heappop(weights)
        y = heapq.heappop(weights)

        tmp = x+y
        result += tmp

        heapq.heappush(weights, tmp) # 덩이의 무게를 다시 넣는 과정이 필요하기 때문에 heapq를 쓰는듯

    return result


n = int(input())
weights = list(map(int, input().split()))

heapq.heapify(weights)

print(getMinForce(weights))


