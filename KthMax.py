a=input().split()
n=int(a[1])
a=input().split()
a=[int(d) for d in a]
a.sort(reverse=1)
print(a[n-1])
