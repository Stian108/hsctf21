# Angr Management

## Description
Author: Josch

The latest celebrity gossip is that a famous movie star is going into a angr management program, but I can't find out who because I need a password to get in... Maybe you can help me?

### Hint
If something seems too hard to do by hand it can probably be automated

## Solution
As the title of the challenge alludes to this is a perfect challenge for Angr. 
```py
import angr,sys

def main():
    proj = angr.Project('../management')
    init_state = proj.factory.entry_state()
    simulation = proj.factory.simgr(init_state)

    simulation.explore(find=is_successful, avoid=should_abort)

    if simulation.found:
        solution = simulation.found[0]
        print('flag: ', solution.posix.dumps(sys.stdin.fileno()))
    else:
        print('no flag')

def is_successful(state):
    return b"CORRECT!" in state.posix.dumps(sys.stdout.fileno())

# set disexpected function
def should_abort(state):
    return b"WRONG" in state.posix.dumps(sys.stdout.fileno())

if __name__ == '__main__':
    main()
```