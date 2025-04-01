from secrets import randbelow

class FibonacciCipher:
    def __init__(self, base1:int=None, base2:int=None, rand:int=256):
        self.base1 = base1 or randbelow(rand)
        self.base2 = base2 or randbelow(rand)
        self.base=[base1, base2]

    def reset(self):
        self.base = [self.base1, self.base2]

    def new(self, base1, base2):
        self.base1 = base1
        self.base2 = base2
        self.reset()
    
    def _fibonacci(self, n):
        for _ in range(n - 2):
            self.base.append(self.base[-1] + self.base[-2])

    def _cipher(self, text, shift):
        return ''.join(chr((ord(char)+shift[i])%256) for i, char in enumerate(text))
    
    def encrypt(self, text):
        self.reset()
        self._fibonacci(len(text))
        shift_values = self.base
        return self._cipher(text,shift_values)
    
    def decrypt(self, text):
        self.reset()
        self._fibonacci(len(text))
        shift_values = [-x for x in self.base]
        return self._cipher(text,shift_values)

# Example Usage:
cipher = FibonacciCipher()
text ="Hello, World! 12345678"
encrypted = cipher.encrypt(text)
decrypted = cipher.decrypt(encrypted)
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
