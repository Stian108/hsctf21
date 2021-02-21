# Format String 100

## Description
Author: Josch

The Echonator-3000 is the number 1 cutting edge echo machine, any input will be echoed back to the user with full support for fancy format strings!

nc formatstring.heltsikker.no 9004

### Hint
How does format strings work?

## Solution
It seems the server is just passing our input to a `printf` with the flag as the second parameter, so to solve this we simply pass the format option for strings `%s`

```
HSCTF{never_trust_user_input!}
```