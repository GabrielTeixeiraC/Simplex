jal x1, Collatz
jal x0, End

Collatz:
	addi x5, x0, 1 # x5 = i = 1
    addi x6, x0, 1 # x6 = 1
    addi x7, x11, 0 # x7 = initialValue
    addi x8, x0, 2 # x8 = 2
    addi x9, x0, 3 # x9 = 3
    beq x0, x0, Loop

Loop:
	beq x5, x10, ReturnV # i == n
    beq x7, x6, ReturnZ # initialValue == 1
    rem x29, x7, x8 # x29 = initialValue % 2
    beq x29, x0, Even # if initialValue is even
    beq x0, x0, Odd
    
ReturnV:
	addi x10, x7, 0 # x10 = initialValue at iteration n
    jalr x0, 0(x1) # return

ReturnZ:
	addi x10, x0, 0 # x10 = 0
    jalr x0, 0(x1) #return
    
Even:
	div x7, x7, x8 # initialValue = initialValue / 2
    addi x5, x5, 1 # i++
    beq x0, x0, Loop
    
Odd:
	mul x7, x7, x9 # initialValue = initialValue * 3
    addi x7, x7, 1 # initialValue = initialValue + 1
    addi x5, x5, 1 # i++
    beq x0, x0, Loop
   
End:
