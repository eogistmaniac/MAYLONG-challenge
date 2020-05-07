n = int(input())
g =[]
for i in  range(n):
    n = int(input())
    l = list(map(int,input().split()))
    u = 1
    for k in range(len(l)-1):
        s = abs(l[k]-l[k+1])
        if(s<=2):
            u = u+1
        else:
            g.append(u)
            u = 1
    g.append(u)
    print(min(g),max(g))
    g =[]