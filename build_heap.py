# python3

def sift_down(n, data, i, swap, swaps):
    index = i
    l = 2 * i + 1
    if l < n and data[l] < data[index]:
        index = l
    r = 2 * i + 2
    if r < n and data[r] < data[index]:
        index = r
    if i != index:
        data[i], data[index] = data[index], data[i]
        swap += 1
        swaps.append((i, index))
        swap, swaps = sift_down(n, data, index, swap, swaps)
    return swap, swaps

def build_heap(n, data):
    swap = 0
    swaps = []
    for i in range(n // 2, -1, -1):
        swap, swaps = sift_down(n, data, i, swap, swaps)
    return swap, swaps

def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swap, swaps = build_heap(n, data)
    
    print(swap)
    for sw in swaps:
        print(sw[0], sw[1])

if __name__ == "__main__":
    main()
