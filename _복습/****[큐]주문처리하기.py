from collections import deque

class orderInfo:
    def __init__ (self, visit, process, is_vip):
        self.visit = visit
        self.process = process
        self.is_vip = is_vip

def processOrder(orders):
    current = 0
    index = 0
    result = []
    vip = deque()
    normal = deque()

    while index < len(orders) or vip or normal:
        while index <len(orders) and orders[index].visit <= current:   # 이미 방문한 손님들이 있다면, queue에 각각 담아야함
            order = orders[index]
            if order.is_vip == 1:
                vip.append((order.process, index))
            else:
                normal.append((order.process, index))
            index += 1

        # 다 담았으면 주문 처리해야함
        if vip:
            duration, idx = vip.popleft()
        elif normal:
            duration, idx = normal.popleft()
        else: # 아직 도착하지 않은 주문이 남아있어서 시간이 흘러야 한다면, 현 인덱스 주문시간으로 시간을 점프
            current = orders[index].visit
            continue    # 이 컨티뉴를 하면

        result.append(idx+1)
        current += duration

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


