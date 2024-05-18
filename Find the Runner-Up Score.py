if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    if n > 1:
        unique = list(set(arr))
        unique.sort()
                
        if len(unique) > 1:
            print(unique[-2])
        else:
            print("no runner up")
    else:
        print("no runner up")
