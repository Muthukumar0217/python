n,q=(map(int,input().split()))
s=0
for i in range(1,n+1):
    if i==q:
        break
    else:
        s=s+i
print(s)
