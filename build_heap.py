# python3

from math import floor

def build_heap(n, data):
    swap = 0
    swaps = []
    size = n - 1
    for i in range(floor(n/2), -1, -1):
        swap, swaps, data = sift_down(i, size, data, swap, swaps)  
    return swap, swaps


def main():

    n = int(input())
    data = list(map(int, input().split()))

    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
