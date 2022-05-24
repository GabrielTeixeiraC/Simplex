import numpy as np

N, M = input().split()    # number of restrictions and variables
N = int(N)
M = int(M)

numColumns = M + N
c = np.zeros(numColumns)    # objective function + operations log
b = np.zeros(N)        # restrictions
I = np.eye(N)   
zerosA = np.zeros((N, M))
A = np.concatenate((I, zerosA), axis=1)    # matrix of restrictions + operations log

cStr = input().split()
restrictions = []

for i in range(N):
    restrictions.append(input().split())

for j in range(M):
    c[M + j] = float(cStr[j])
    
for i in range(N):
    for j in range(M):
        A[i][M + j] = float(restrictions[i][j])
    b[i] = float(restrictions[i][M])
b = b.reshape(N, 1)
auxiliaryA = A
A = np.concatenate((A, b), axis=1)
for i in range(N):
    if (A[i][-1] < 0):
        auxiliaryA[i] *= -1
auxiliaryA = np.concatenate((auxiliaryA, np.eye(N)), axis=1)
auxiliaryA = np.concatenate((auxiliaryA, np.absolute(b)), axis=1)

onesC = np.ones(N)
auxiliaryC = np.concatenate((np.zeros(numColumns), onesC))
auxiliaryC = np.concatenate((auxiliaryC, np.array([0])))


base = list(range(N + M, len(auxiliaryC) - 1))
A = auxiliaryA

# canonical form
def canonicalForm(A, c, base):
    for i in range(len(base)):
        if (A[i][base[i]] != 0):
            A[i, :] /= A[i][base[i]]
        for j in range(N):
            if (i != j):
                aPivot = A[j][base[i]] * -1
                A[j, :] += A[i, :] * aPivot
        cPivot = c[base[i]] * -1
        c += A[i, :] * cPivot

def findPivotToEnterBase(A, c):
    for j in range(N, len(c)):
        columnIndex = j
        lineIndex = 0
        if (c[columnIndex] < 0):
            min =  1000
            lineIndex = 0
            for i in range(N):
                value = 1000
                if (A[i][columnIndex] != 0):
                    value = A[i][-1]/A[i][columnIndex]
                if(value < min and value > 0):
                    min = value
                    lineIndex = i
            break
    return lineIndex, columnIndex

def printC(c):
    for i in range(len(c)):
        print(round(c[i],2), end='\t')
    print()
    print()

def printA(A):
    for i in range(len(A)):
        for j in range(len(A[0])):
            print(round(A[i][j], 2), end='\t')
        print()
    print()

printC(auxiliaryC)
printA(auxiliaryA)
canonicalForm(A, auxiliaryC, base)
printC(auxiliaryC)
printA(auxiliaryA)
while(np.any(auxiliaryC[N:] < 0)):
    printC(auxiliaryC)
    printA(auxiliaryA)
    lineIndex, columnIndex = findPivotToEnterBase(A, auxiliaryC)
    base[lineIndex] = columnIndex
    canonicalForm(A, auxiliaryC, base)
printC(auxiliaryC)
printA(auxiliaryA)