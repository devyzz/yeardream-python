'''
백준 21736번 헌내기는 친구가 필요해 (BFS)
백준 1966번 프린터 큐
프로그래머스 "공항 대기열 시뮬레이션"
백준 3190번 뱀 (시뮬레이션 + 시간흐름)

[문제 만나면 바로 이 순서!]
1. "시간 흐름"이 있는가? → 시뮬레이션
2. "우선순위 조건"이 있는가? → 분기 조건 체크
3. "큐처럼 들어오는 데이터"인가? → 큐나 리스트 사용
4. "언제 어떤 데이터가 들어오고 처리되는가?" → 시간 기준 이벤트 정리
5. 슈도코드 써보면서 흐름 정리

주문처리 슈도코드

- 현재시간 = 0
- index = 0 (다음 주문을 가리키는 포인터)
- VIP 큐, 일반 큐 나눠서 생성
- 처리 순서를 저장할 리스트 생성

- 반복문 (모든 주문을 처리할 때 까지)
    - 현재 시간까지 도착한 주문을 큐에 나눠담기
        - VIP -> vip큐
        - normao -> normal큐
        - index 증가
    - 처리할 주문 고르기 :
        1. vip queue에 있는 것들 pop
        2. normal queue에 있는 것들 pop
        3. 아무것도 없으면 다음 주문시간으로 점프
    - 처리한 시간만큼 현재시간 증가
    - 처리된 주문번호 기록

'''
from collections import deque

class orderInfo:
    def __init__(self, v_time, p_time, is_vip):
        self.v_time = v_time  # 도착 시간
        self.p_time = p_time  # 처리 시간
        self.is_vip = is_vip  # VIP 여부 (1: VIP, 0: 일반)

def processOrder(orders):
    '''
    주문 정보가 주어질 때, 주문이 처리되는 순서를 반환합니다.
    '''

    normal_queue = deque()
    vip_queue = deque()
    result = []
    current_time = 0
    index = 0
    total_orders = len(orders)

    while index < total_orders or vip_queue or normal_queue:    #최초의 루프는 index < total_orders로 돌고, vip, normal에 나눠담긴 이후부터는 vip, normal의 개수로 loop를 돔
        # 현재 시간까지 도착한 주문 큐에 추가
        while index < total_orders and orders[index].v_time <= current_time:  # 현재 시간 이하로 도착한 주문들을 모두 VIP/일반 큐에 넣는다.
            order = orders[index]
            if order.is_vip == 1:   # vip주문이라면 vip큐로 들어가게
                vip_queue.append((order.p_time, index))  # 처리시간, 인덱스
            else:                   # 일반 주문이라면 일반 큐로
                normal_queue.append((order.p_time, index))
            index += 1 # 인덱스를 늘려가면서 일단 주문을 노말큐 / 인덱스큐로 나눠담음

        # 처리할 주문 선택
        if vip_queue:   #vip큐가 먼저 돌아져야함
            duration, idx = vip_queue.popleft()
        elif normal_queue:
            duration, idx = normal_queue.popleft()
        else:
            # 아직 도착하지 않은 주문이 있다면 도착 시간까지 점프
            current_time = orders[index].v_time
            continue

        result.append(idx + 1)  # 주문 번호는 1부터 시작
        current_time += duration  # 처리 시간만큼 경과

    return result

def main():
    p = int(input())  # 주문 수

    orders = []

    for _ in range(p):
        v_time, p_time, is_vip = map(int, input().split())
        orders.append(orderInfo(v_time, p_time, is_vip))

    print(*processOrder(orders))  # 결과 출력

if __name__ == "__main__":
    main()
