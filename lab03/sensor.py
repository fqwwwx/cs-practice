porog=float(input())
n=int(input())
err = 0
above = 0
a = []
for i in range(n):
    x = input()
    if x == 'error':
        err += 1 
    else:
        x=float(x)
        a.append(x)
        if x > porog:
            above +=1
print(n)
print(err)
print(above)
print(f"{max(a):.1f}")
print(f"{sum(a) / len(a):.1f}")