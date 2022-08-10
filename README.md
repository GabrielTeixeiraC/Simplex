# Simplex
This program implements the Simplex algorithm, used to solve linear programmings defined by:

    max cTx
    subject to Ax ≤ b
    x ≥ 0

The inputs are in the format:

    n m
    c1 c2 . . . cm
    a1,1 a1,2 . . . a1,m b1
    a2,1 a2,2 . . . a2,m b2
    .
    .
    .
    an,1 an,2 . . . an,m bn
    
    ∀i, 1 ≤ i ≤ n, ∀j, 1 ≤ j ≤ m, |ai,k| ≤ 20
    ∀i, 1 ≤ i ≤ m, |bi| ≤ 100
    ∀i, 1 ≤ i ≤ m, |ci| ≤ 10

There are three possible outputs:

    • In case the LP has an optimal value:
        otima
        solution (x)
        certificate of optimality
    • In case the LP is unfeasible:
        inviavel
        certificate of infeasibility
    • In case the LP is unlimited:
        unlimited
        a viable solution
        unlimited LP certificate

## Example 1:

### Input: 
    3 3
    2 4 8
    1 0 0 1
    0 1 0 1
    0 0 1 1

### Output
    otima
    14
    1 1 1
    2 4 8

## Example 2:

### Input: 
    4 3
    1 1 1
    1 0 0 -1
    0 1 0 -1
    0 0 1 -1
    1 1 1 -1

### Output
    inviavel
    1 1 1 1

## Example 3:

### Input: 
    2 3
    1 0 0
    -1 1 0 5
    -1 0 1 7

### Output
    ilimitada
    0 5 7
    1 1 1
