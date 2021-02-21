# Bash playground

## Description
Author: jalgroy

We set up a server for you to practice your bash scripting!

Login: ssh guest@bp.heltsikker.no

Password: guest

Note: We've disabled access to other programs so you can't read any secret information. But you are free to do bash scripting in the shell!

### Hint
The flag is stored in a file named flag.txt

## Solution
Programs are disabled, but luckily bash has `read`

```bash
while read line
do
    echo "$line"
done < /flag.txt
```

```
HSCTF{gr3@t_b@5h_sk1llzzzz}
```