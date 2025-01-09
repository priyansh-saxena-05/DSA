n, x = map(int, input().split())
weight = list(map(int, input().split()))


weight.sort()
count = 0
i, j = 0, n - 1

while i <= j:
    if weight[i] + weight[j] <= x:
        i += 1
    j -= 1
    count += 1

print(count)