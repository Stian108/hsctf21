# Breaker

## Description
Author: Josch

I can't seem to find the password for this application in the strings? Maybe there is some other way to find the correct input...


### Hint
Maybe you can understand the general flow of the program without understanding every line of assembly?

## Solution
Fire up GDB. With `disass main` we can see that there is a call to strcmp at `main+110` so lets set a breakpoint there with `b *main+100`. We can also see that before this call the parameters are loaded into `$rsi` and `$rdi`. Run the program with `r` and give it any input. It will now stop at the breakpoint we set. Check what the registers we noted contain now to see what is being compared. `x/s $rsi` gives us back the input we wrote and `x/s $rdi` gives us the flag:

```
HSCTF{you_dont_always_have_to_understand_the_code_to_reverse_it}
```