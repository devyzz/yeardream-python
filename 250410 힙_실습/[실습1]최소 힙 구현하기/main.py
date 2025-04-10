from priority_queue2 import PriorityQueue

def main():
    myPQ = PriorityQueue()

    n = int(input())

    for i in range(n):
        line = [int(v) for v in input().split()]
        if line[0] == 0:
            myPQ.push(line[1])
        elif line[0] == 1:
            myPQ.pop()
        elif line[0] == 2:
            print(myPQ.top())


if __name__ == "__main__":
    main()
