from heapsort import heapSort

def main():
    '''
    Do not change this code
    '''

    line = [int(x) for x in input().split()]

    print(*heapSort(line))

if __name__ == "__main__":
    main()



