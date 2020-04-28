def result(bars, num, d, m):
    count = 0
    for i in range(0,bars):
        total = sum(num[i:i+m])
        if total == d:
            count+=1
    return count

bars = int(input())

num = [int(x) for x in input().split()]
d, m = map(int, input().split())
print(result(bars, num, d, m))

