def z_algorithm(s):
    N = len(s)
    Z = [0] * N
    Z[0] = N
    i = 1
    j = 0
    while i < N:
        while i + j < N and s[j] == s[i + j]:
            j += 1
        Z[i] = j
        if j == 0:
            i += 1
            continue
        k = 1
        while k < j and k + Z[k] < j:
            Z[i + k] = Z[k]
            k += 1
        i += k
        j -= k
    return Z