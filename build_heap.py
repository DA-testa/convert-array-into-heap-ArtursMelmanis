# python3

from math import floor

def build_heap(n, data):
    swap = 0
    swaps = []
    size = n - 1
    for i in range(floor(n/2), -1, -1):
       swap, swaps, data = sift_down(i, size, data, swap, swaps)
    return swap, swaps
    
def sift_down(i, size, data, swap, swaps):
    index = i
    l = LeftChild(i + 1)
    if l <= size and data[l] < data[index]:
        index = l
    r = RightChild(i + 1)
    if r <= size and data[r] < data[index]:
        index = r
    if i != index:
        data[i], data[index] = data[index], data[i]
        swap += 1
        swaps.append((i, index))
        swap, swaps, data = sift_down(index, size, data, swap, swaps)
    return swap, swaps, data

def LeftChild(i):
    return 2 * i - 1
def RightChild(i):
    return 2 * i

def main():
    n = input().strip()
    if not n.isdigit():
        print("Invalid input")
        return
    
    n = int(n)
    data = input().strip().split()
    if len(data) != n:
        print("Invalid input")
        return
    
    try:
        data = [int(x) for x in data]
    except ValueError:
        print("Invalid input")
        return
    
    swap, swaps = build_heap(n, data)
    
    print(swap)
    for swap in swaps:
        print(swap[0], swap[1])

if __name__ == "__main__":
    main()
