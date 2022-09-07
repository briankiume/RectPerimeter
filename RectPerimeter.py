def minPeri(n):
    factors = []
    for x in range(1, n + 1):
        if n % x == 0:
            factors.append(x)

    all = []
    for x in range(len(factors)):
        i = factors[x]
        j = factors[-1 - x]
        if i not in all:
            all.append(i)
        if j not in all:
            all.append(j)

    pairs = []
    for x in range(0, len(all), 2):
        pairs.append((all[x], all[x + 1]))

    perimeters = []
    for pair in pairs:
        perimeter = 2 * (pair[0] + pair[1])
        perimeters.append(perimeter)

    min_peri = min(perimeters)
    return min_peri


print(minPeri(30))
