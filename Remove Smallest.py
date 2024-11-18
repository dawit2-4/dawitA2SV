def remove_smallest():
    t = int(input()) 
    for _ in range(t):
        n = int(input())  
        arr = list(map(int, input().split()))  
        
        arr.sort() 
        
 
        possible = True
        for i in range(len(arr) - 1):
            if arr[i+1] - arr[i] > 1:
                possible = False
                break
        
        print("YES" if possible else "NO")
 
 
remove_smallest()
