if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr=set(arr)
    arr=list(arr)
    arr.remove(max(arr))
    print(max(arr))