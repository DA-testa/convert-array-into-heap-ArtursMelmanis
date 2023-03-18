# python3

def build_heap(n, data):
    swap = 0
    swaps = []
    size = n - 1
    for i in range((n // 2), -1, -1, -1):
        k = i
        v = data[k]
        heap = False
        while not heap and 2 * k + 1 <= size:
            j = 2 * k + 1
            if j < size and data[j] > data[j + 1]:
                j += 1
            if v <= data[j]:
                heap = True
            else:
                data[k] = data[j]
                swap += 1
                swaps.append((k, j))
                k = j
            data[k] = v
        
    return swap, swaps
    
def main():
    
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n
    swap, swaps = build_heap(n, data)
    print(swap)
    
    for swap in swaps:
        print(swap[0], swap[1])

if __name__ == "__main__":
    main()
