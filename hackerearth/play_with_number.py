def main():
    N = int(input("enter the total elemants of the array"))
    Q = int(input("enter the total query"))
    a = []

    for i in range (1,N+1):
        a.append(int(input()))

    for j in range (0,Q):
        l = int(input())
        h = int(input())
        for i in range (l,h+1):
            sum = sum + a[i]
            