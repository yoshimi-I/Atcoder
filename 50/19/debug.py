def solver(X, K, D):
    for i in range(K):
        X = abs(X)-D
    return abs(X)

