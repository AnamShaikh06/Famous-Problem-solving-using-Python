li = input().split(',')

pairs = []

for i in range(len(li)):
    x, y = map(int, li[i].split())
    pairs.append([x, y])

# sort by first, then second
pairs.sort()

print(pairs)
