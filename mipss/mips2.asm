.data
str:.ascii "abcd"
strn:.asciiz "abcdefg"
b0:.byte 1,2,3,4,5
h0:.half 1,2,3,4
w0:.word 1,2,3,4
w1:.word str,strn,b0,h0,w0
.text
main:
li $v0,1
li $a0,0x200
syscall  #输出十进制数521
li $v0,4
la $a0,str
syscall  #输出字符串str
la $a0,strn
syscall  #输出字符串strn
li $v0,5
syscall #输入十进制整数
li $v0,8
la $a0,b0
li $a1,5
syscall  #输出字符串
li $v0,10
syscall  #程序结束