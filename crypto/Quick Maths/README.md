# Quick Maths

## Description
Author: Josch

2 + 2 is 4, but what's the following message XOR'ed with the decimal digit 3?

```
KP@WEx{lq\kltfufq\abpjh\jp\pwjoo\bm\jnslqwbmw\sbqw\le\nlgfqm\hqzswl~
```

### Hint
CyberChef is a great tool for working with text encodings and encryptions

## Solution
Well the hint is right about that. The description is pretty clear at what to do, we just have to find the right [recipe](https://gchq.github.io/CyberChef/#recipe=XOR(%7B'option':'Decimal','string':'3'%7D,'Standard',false)&input=S1BAV0V4e2xxXGtsdGZ1ZnFcYWJwamhcanBccHdqb29cYm1cam5zbHF3Ym13XHNicXdcbGVcbmxnZnFtXGhxenN3bH4)

```
HSCTF{xor_however_basik_is_still_an_important_part_of_modern_krypto}
```