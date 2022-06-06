jal x1, RecSelection

RecSelection:
	addi x5, x0, 1 # x5 = 1
	blt x5, x11, Recursive # if x11 > 1, recurse
    jal x1, End # else, end procedure

Recursive:
	jal x1, FindMaxIndex # call to FindMaxIndex(array, nelem)
    slli x6, x6, 2 # pos * 4 
    addi x27, x11, -1 # nelem - 1
    slli x28, x27, 2 # (nelem - 1) * 4
    add x29, x10, x6 # x29 = array[pos]
    add x30, x10, x28 # x30 = array[nelem - 1]
    lw x7, 0(x29) # x7 = array[pos] 
    lw x8, 0(x30) # x8 = array[nelem - 1]
    sw x8, 0(x29) # array[pos] = array[nelem - 1]
    sw x7, 0(x30) # array[nelem - 1] = array[pos]
	addi x11, x11, -1 # nelem--
    jal x1, RecSelection # call to RecSelection(array, nelem - 1)

FindMaxIndex:
    addi x26, x0, 0 # i
    addi x27, x0, 0	# max
    addi x28, x0, 0	# maxIndex
	beq x0, x0, Loop

Loop:
	beq	x26, x11, ReturnI # if i == nelem, return maxIndex
    slli x29, x26, 2 # i * 4
    add x30, x10, x29 # array[i]
    lw x31, 0(x30) # x31 = array[i] 
    blt x27, x31, SaveIndex
    addi x26, x26, 1 #i++
    beq x0, x0, Loop

SaveIndex:
	lw x27, 0(x30) # max = array[i]
    addi x28, x26, 0 # maxIndex = i
	addi x26, x26, 1 # i++
    beq x0, x0, Loop
    
ReturnI:
	addi x6, x28, 0 # x6 = maxIndex
    jalr x0, 0(x1) # return to Recursive
    
End:
