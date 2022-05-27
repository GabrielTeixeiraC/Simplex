import numpy as np

def zero(value):
    if (abs(value) < 1e-4):
        value = 0.0
    return value

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
    vfunc = np.vectorize(zero)
    A = vfunc(A)
    c = vfunc(c)
    return A, c

def findPivotToEnterBase(A, c):
    N = A.shape[0]
    for j in range(N, len(c)):
        unbounded = False
        columnIndex = j
        lineIndex = 0
        if (c[columnIndex] < 0):
            if (np.all(A[:, columnIndex] <= 0)):
                unbounded = True
                break
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
    return lineIndex, columnIndex, unbounded

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

def findSolution(A, c, base):
    N = A.shape[0]
    solution = np.zeros(len(c) - N)
    for i in range(len(base)):
        solution[base[i] - N] = A[i][-1]
    return solution

def simplex(A, c, base):
    printC(c)
    printA(A)
    A, c = canonicalForm(A, c, base)
    printC(c)
    printA(A)
    while(np.any(c[N:len(c) - 1] < 0)):
        printC(c)
        printA(A)
        lineIndex, columnIndex, unbounded = findPivotToEnterBase(A, c)
        if (unbounded):
            d = np.zeros(M + N)
            d[columnIndex - N] = 1
            for i in range(len(base)):
                d[base[i] - N] = -1 * A[i][columnIndex]
            certificate = d
            optimal = 'unbounded'
            solution = findSolution(A, c, base)
            return certificate, optimal, solution

        base[lineIndex] = columnIndex
        A, c = canonicalForm(A, c, base)
    while(np.any(A[:, -1] < 0)):
        A, c, base = dualSimplex(A, c, base)
        A, c = canonicalForm(A, c, base)
        printC(c)
        printA(A)
    printC(c)
    printA(A)
    solution = findSolution(A, c, base)
    
    certificate = c[:N]
    optimal = c[-1]
    return certificate, optimal, solution

def dualSimplex(A, c, base):
    N = A.shape[0]
    M = A.shape[1] - 1
    b = A[:, -1]
    lineIndex = -1
    columnIndex = -1
    for i in range(N):
        if(b[i] < 0):
            lineIndex = i
            break
    if(lineIndex == -1):
        return A, c, base
    minimum = 1000
    for j in range(N, M):
        if(A[lineIndex][j] < 0):
            value = c[j]/(A[lineIndex][j] * -1)
            if(value < minimum):
                minimum = value
                columnIndex = j
    base[lineIndex] = columnIndex
    return A, c, base   

def printArray(array):
    for i in range(len(array)):
        print('{:.7f}'.format(array[i]), end=' ')
    print()

N, M = input().split()    # number of restrictions and variables
N = int(N)
M = int(M)

cStr = input().split()
restrictions = []

for i in range(N):
    restrictions.append(input().split())

restrictions = np.array(restrictions, dtype=float)

c = np.array(cStr, dtype=float) * -1
b = np.array(restrictions[:, -1])
A = np.array(restrictions[:,:-1])

b = b.reshape(N, 1)

A = np.concatenate((A, np.eye(N)), axis=1)
A = np.concatenate((np.eye(N), A), axis=1)

for i in range(N):
    if (b[i] < 0):
        b[i] *= -1
        A[i] *= -1

auxiliaryA = np.concatenate((A, np.eye(N)), axis=1)
auxiliaryA = np.concatenate((auxiliaryA, b), axis=1)

A = np.concatenate((A, b), axis=1)

numColumnsAuxiliary = auxiliaryA.shape[1]

auxiliaryC = np.zeros(numColumnsAuxiliary)
auxiliaryC[numColumnsAuxiliary - (N + 1):-1] = 1

auxiliaryBase = list(range(numColumnsAuxiliary - (N + 1), numColumnsAuxiliary - 1))

certificate, optimal, solution = simplex(auxiliaryA, auxiliaryC, auxiliaryBase)

if(optimal < 0):
    print("inviavel")
    printArray(certificate)
else:
    numColumns = A.shape[1]
    c = np.concatenate((np.zeros(N), c))
    c = np.concatenate((c, np.zeros(N)))
    c = np.concatenate((c, np.array([0])))
    base = list(range(numColumns - (N + 1), numColumns - 1))
    certificate, optimal, solution = simplex(A, c, base)
    if(optimal == 'unbounded'):
        print("ilimitada")
        printArray(solution[:M])
        printArray(certificate[:M])

    else:
        print("otima")
        print('{:.7f}'.format(optimal))
        printArray(solution[:M])
        printArray(certificate)