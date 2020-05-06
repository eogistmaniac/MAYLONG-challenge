for _ in range(int(input())):
    x, y = map(int, input().split())
    string = input()
    for k in range(y):
        l = []
        c = 0
        noisc = int(input())
        for j in range(len(string)):
            if l.count(string[j]) < noisc:
                l.append(string[j])
            else:
                c = c + 1
        print(c)