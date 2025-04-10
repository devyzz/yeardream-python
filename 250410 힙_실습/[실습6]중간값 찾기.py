# n개의 숫자가 차례대로 주어질 때, 매 순간마다 “지금까지 입력된 수 중에서 중간값”을 반환하는 프로그램을 작성하세요.
'''
10
1 2 3 4 5 6 7 8 9 10
-->
1 1 2 2 3 3 4 4 5 5
'''

import heapq

def find_mid(numbers):
    left = []   # 최대 힙 (중간값 이하)
    right = []  # 최소 힙 (중간값 초과)

    result = []

    for number in numbers:
        #왼쪽 힙은 최대 힙 -> 파이썬은 최소 힙만 제공하므로 음수로 넣음
        if not left or number <= -left[0]:
            heapq.heappush(left, -number)
        else:
            heapq.heappush(right, number)

        #힙 크기 맞추기 (왼쪽이 항상 같거나 1개 더 많게)
        if len(left) > len(right) + 1:
            heapq.heappush(right, -heapq.heappop(left))
        elif len(right) > len(left):
            heapq.heappush(left, -heapq.heappop(right))

        # Step 3. 중간값은 항상 왼쪽 힙의 루트
        result.append(-left[0])

    return result

# 실행부
n = int(input())
numbers = list(map(int, input().split()))
print(*find_mid(numbers))
