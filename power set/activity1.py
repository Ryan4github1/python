def powerset(s):
    """Return the powerset of a set s using binary representation. """
    s = list(s)
    n = len(s)
    result = []
    for i in range(1<<n):
        subset = [s[j] for j in range(n) if (i & (1 << j))]
        result.append(subset)
    return result
answer = powerset({22,89,67})
print(answer)