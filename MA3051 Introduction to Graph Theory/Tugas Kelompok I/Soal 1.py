def mat_self_mul(A, B):
    C = [[0] * len(A) for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            C[i][j] = 0
            for k in range(len(A[0])):
                C[i][j] = C[i][j] + A[i][k] * B[k][j]
    
    return C

def walk(adj_mat, len_walk, a, b):
    if len_walk == 0:
        return int(a == b)
    B = [row[:] for row in adj_mat]
    for i in range(1, len_walk):
        B = mat_self_mul(B, adj_mat)
    
    return B[a][b]

A = [[0, 0, 0, 1, 0, 0, 0, 0],
              [0, 0, 1, 0, 1, 0, 0, 0],
              [0, 1, 0, 1, 1, 1, 0, 0],
              [1, 0, 1, 0, 1, 1, 0, 0],
              [0, 1, 1, 1, 0, 1, 0, 0],
              [0, 0, 1, 1, 1, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 1],
              [0, 0, 0, 0, 0, 0, 1, 0]]

k = int(input("Masukkan panjang walk : "))
u, v = map(int,input("Masukktan 2 titik yang ingin dicari walknya : ").split())
banyak_walk = walk(A, k, u, v)
print(f"banyak walk dari u ke v dengan panjang k: {banyak_walk}")



