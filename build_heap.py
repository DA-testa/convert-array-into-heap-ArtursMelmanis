# python3

def sift_down(i, data, swaps):
    n = len(data)
    index = i
    l = 2 * i + 1
    if l < n and data[l] < data[index]:
        index = l
    r = 2 * i + 2
    if r < n and data[r] < data[index]:
        index = r
    if i != index:
        swaps.append((i, index))
        data[i], data[index] = data[index], data[i]
        sift_down(index, data, swaps)

def build_heap(data):
    swaps = []
    n = len(data)
    for i in range(n // 2 -1, -1, -1):
        sift_down(data, n, i, swaps)
    return swaps

def main():
    txt = input()
    if "I" in txt:
        n = int(input())
        data = list(map(int, input().split()))
    if "F" in txt:
        f = input()
        with open("tests/" + f, 'r') as file:
            n = int(file.readline())
            data = list(map(int, file.readline().split()))
    assert len(data) == n
    swaps = build_heap(data)
    print(len(swaps))
    for sw in swaps:
        print(sw[0], sw[1])

if __name__ == "__main__":
    main()
