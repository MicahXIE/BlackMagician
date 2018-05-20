# x y z n input 1 1 1 2  0<=i<=x 0<=j<=y 0<=k<=z x+y+z!=n 
# [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    res = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if (i+j+k) != n ]
    print(res)
