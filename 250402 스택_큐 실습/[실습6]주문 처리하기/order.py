from collections import deque
'''
함수 processOrder를 구현하세요.
'''

class orderInfo:
    '''
    이 부분은 수정하지 마세요.
    '''
    def __init__(self, t, d, v):
        self.time = t
        self.duration = d
        self.vip = v

def processOrder(orders) :
    '''
    주문 정보가 주어질 때, 주문이 처리되는 순서를 반환합니다.
    '''

    normal_queue = deque()  # 일반 고객 주문
    vip_queue = deque()  # VIP 고객 주문
    result = []
    now = 0  # 현재 시간
    i = 0  # 처리할 주문 인덱스

    while i < len(orders) or normal_queue or vip_queue:
        while i < len(orders) and orders[i].time <= now:
            if orders[i].vip == 1:
                vip_queue.append((orders[i].time, orders[i].duration, i))
            else:
                normal_queue.append((orders[i].time, orders[i].duration, i))
            i += 1

        if vip_queue:
            _, duration, idx = vip_queue.popleft()  
        elif normal_queue:
            _, duration, idx = normal_queue.popleft() 
        else:
            now = orders[i].time
            continue

        result.append(idx + 1)  
        now += duration
    return result