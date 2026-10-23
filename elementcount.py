n = int(input())
l = list(map(int,input().split()))
d1 = {}
d2 = {}
for i in l:
    if i in d1:
        d1[i] += 1
    else:
        d1[i] = 1
d2 = dict(sorted(d1.items()))
for k,v in d2.items():
    print(k,": ",v)