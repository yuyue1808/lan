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
syscall  #���ʮ������521
li $v0,4
la $a0,str
syscall  #����ַ���str
la $a0,strn
syscall  #����ַ���strn
li $v0,5
syscall #����ʮ��������
li $v0,8
la $a0,b0
li $a1,5
syscall  #����ַ���
li $v0,10
syscall  #�������