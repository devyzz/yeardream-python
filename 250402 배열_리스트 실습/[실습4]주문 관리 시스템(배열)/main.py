from orderManager import orderManager


def main():

    line = [int(v) for v in input().split()]
    m = line[0]

    manager = orderManager()

    for i in range(m):
        line = [int(v) for v in input().split()]

        if line[0] == 1:
            manager.addOrder(line[1])

        elif line[0] == 2:
            manager.removeOrder(line[1])

        elif line[0] == 3:
            myOrder = manager.getOrder(line[1])

            if myOrder == -1:
                print("-1")
            else:
                print(str(manager.getOrder(line[1])))


if __name__ == "__main__":
    main()

