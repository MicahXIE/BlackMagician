# n number of score elements e.g 5
# arr score sheet 2 3 6 6 5 to [2,3,6,6,5]
# target find the runner-up score e.g 5

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    lis = list(arr)[:n]
    z = max(lis)
    while max(lis) == z:
        lis.remove(max(lis))
        
    print (max(lis))
