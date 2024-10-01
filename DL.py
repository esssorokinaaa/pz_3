import sys
sys.setrecursionlimit(10000)  # Для избежания превышения рекурсивного ограничения

INF = float('inf')

def DamerauLevenshteinDistance(S, T, deleteCost=1, insertCost=1, replaceCost=1, transposeCost=1):
    M = len(S)
    N = len(T)
    
    D = [[INF] * (N+1) for _ in range(M+1)]
    
    # База индукции
    D[0][0] = 0
    for i in range(M):
        D[i+1][0] = D[i][0] + deleteCost
    for j in range(N):
        D[0][j+1] = D[0][j] + insertCost
    
    lastPosition = {}
    
    for letter in set(S).union(set(T)):
        lastPosition[letter] = 0
    
    for i in range(M):
        last = 0
        for j in range(N):
            iPrime = lastPosition[T[j]]
            jPrime = last
            
            if S[i] == T[j]:
                D[i+1][j+1] = D[i][j]
                last = j
                
            else:
                D[i+1][j+1] = min(D[i][j] + replaceCost, D[i+1][j] + insertCost, D[i][j+1] + deleteCost)
                
            costTransposition = D[iPrime][jPrime] + (i - iPrime - 1) * deleteCost + transposeCost + (j - jPrime - 1) * insertCost
            D[i+1][j+1] = min(D[i+1][j+1], costTransposition)
            
        lastPosition[S[i]] = i
        
    return D[M][N]

# Пример использования функции
S = 'kitten'
T = 'sitting'
print(DamerauLevenshteinDistance(S, T))