main:
addi $a0, $0, 4
jal fib
add $v0, $0, $v0
syscall
fib:
addi $sp,$sp,-12
sw $ra, 0($sp)
sw $s1, 4($sp)
sw $a0, 8($sp)
slti $t0, $a0, 2
beq $t0,$0, L1
add $v0, $a0 ,$0
j exit
L1:
add $a0, $a0, -1
jal fib
add $s1, $v0, $0
addi $a0, $a0, -1
jal fib
add $v0,  $v0, $s1
exit:
lw $ra, 0($sp)
lw $s1, 4($sp)
lw $a0, 8($sp)
addi $sp, $sp, 12
jr $ra