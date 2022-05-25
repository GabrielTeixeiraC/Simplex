import numpy as np

# canonical form
def canonicalForm(A, c, base):
    for i in range(len(base)):
        if (A[i][base[i]] != 0):
            A[i, :] /= A[i][base[i]]
        for j in range(len(base)):
            if (i != j):
                aPivot = A[j][base[i]] * -1
                A[j, :] += A[i, :] * aPivot
        cPivot = c[base[i]] * -1
        c += A[i, :] * cPivot
    A = np.around(A, decimals=4)
    c = np.around(c, decimals=4)
    return A, c

# def removeLinearlyDependent(A):
#     for i in range(N):
#         for
#     return A, c

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
                if(value < min and value >= 0 and A[i][columnIndex] > 0):
                    min = value
                    lineIndex = i
            break
    return lineIndex, columnIndex

def printC(c):
    for i in range(len(c)):
        print(c[i], end='\t')
    print()
    print()

def printA(A):
    for i in range(len(A)):
        for j in range(len(A[0])):
            print(A[i][j], end='\t')
        print()
    print()

N, M = input().split()    # number of restrictions and variables
N = int(N)
M = int(M)

cStr = input().split()
restrictions = []

for i in range(N):
    restrictions.append(input().split())

restrictions = np.array(restrictions, dtype=float)

c = np.array(cStr, dtype=float)
b = np.array(restrictions[:, -1])
A = np.array(restrictions[:,:-1])

b = b.reshape(N, 1)

auxiliaryA = np.eye(N)
# A = np.concatenate((A, b), axis=1)
sef = np.eye(N)
for i in range(N):
    if (b[i] < 0):
        b[i] *= -1
        A[i] *= -1
        sef[i] *= -1

auxiliaryA = np.concatenate((auxiliaryA, A), axis=1)
auxiliaryA = np.concatenate((auxiliaryA, sef), axis=1)
auxiliaryA = np.concatenate((auxiliaryA, np.eye(N)), axis=1)
auxiliaryA = np.concatenate((auxiliaryA, b), axis=1)

numColumns = auxiliaryA.shape[1]

auxiliaryC = np.zeros(numColumns)
auxiliaryC[numColumns - (N + 1):-1] = 1


base = list(range(numColumns - (N + 1), len(auxiliaryC) - 1))
A = auxiliaryA


printC(np.around(auxiliaryC, decimals=8))
printA(np.around(auxiliaryA, decimals=8))
canonicalForm(auxiliaryA, auxiliaryC, base)
while(np.any(auxiliaryC[N:len(auxiliaryC) - 1] < 0)):
    printC(np.around(auxiliaryC, decimals=8))
    printA(np.around(auxiliaryA, decimals=8))
    lineIndex, columnIndex = findPivotToEnterBase(auxiliaryA, auxiliaryC)
    base[lineIndex] = columnIndex
    auxiliaryA, auxiliaryC = canonicalForm(auxiliaryA, auxiliaryC, base)
printC(np.around(auxiliaryC, decimals=8))
printA(np.around(auxiliaryA, decimals=8))
print(base)