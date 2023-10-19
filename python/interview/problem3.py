def solve(parent, child):
    if len(child) == 0:
        return True
    if parent == child:
        return True
    el = child[0]
    for ind, c in enumerate(child):
        for idx, cv in enumerate(parent):
            if cv == c:
                return solve(parent[idx + 1:], child[ind + 1:])

    return False


a = solve("abdcefgh", "aeh") # True
print(a)
