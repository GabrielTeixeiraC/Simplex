def selecao_rec(vetor, nelem):
    if nelem > 2:
        pos = max_elem(vetor, nelem)
        print(pos)
        aux = vetor[pos]
        vetor[pos] = vetor[nelem - 1]
        vetor[nelem - 1] = aux
        selecao_rec(vetor, nelem - 1)
    else:
        return

def max_elem(vetor, nelem):
    i = 0
    maior = 0
    maiorInd = 0
    while(True):
        if i == nelem:
            return maiorInd
        if vetor[i] > maior:
            maior = vetor[i]
            maiorInd = i
            i = i + 1
        else:   
            i = i + 1

# create unordered list of numbers
vetor = [1, 5, 3, 2, 4]
selecao_rec(vetor, len(vetor))
print(vetor)