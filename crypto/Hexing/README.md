# Quick Maths

## Description
Author: Josch

I found a flag, but I'm having trouble reading it, can you help me?

```
48 53 43 54 46 7b 61 73 63 69 69 5f 69 73 5f 6d 6f 72 65 5f 72 65 61 64 61 62 6c 65 5f 74 68 61 6e 5f 68 65 78 7d
```

### Hint
CyberChef is a great tool for working with text encodings and encryptions

## Solution
Well the hint is right about that. The title alludes that this is encoded as hex, so let's decode that in [cyberchef](https://gchq.github.io/CyberChef/#recipe=From_Hex('Auto')&input=NDggNTMgNDMgNTQgNDYgN2IgNjEgNzMgNjMgNjkgNjkgNWYgNjkgNzMgNWYgNmQgNmYgNzIgNjUgNWYgNzIgNjUgNjEgNjQgNjEgNjIgNmMgNjUgNWYgNzQgNjggNjEgNmUgNWYgNjggNjUgNzggN2Q)

```
HSCTF{ascii_is_more_readable_than_hex}
```