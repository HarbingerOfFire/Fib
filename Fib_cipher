from secrets import randbelow

class Fib:
    def __init__(self, base0:int=None, base1:int=None, random_value:int=None):
        self.base=[base0 or randbelow(random_value or 256), base1 or randbelow(random_value or 256)]
        self.org=self.base

    def fib(self, index):
        for i in range(2,index+1):
            self.base.append(self.base[i-1]+self.base[i-2])
        return self.base[-1]
    
    def cipher(self, buf:str):
        self.base=self.org #reset the base set
        self.fib(len(buf)) #get the fib sequence values
        new=""
        for i,s in enumerate(buf):
            new+=chr((ord(s)*self.base[i])) #simple transformation
        return new

    def decipher(self, ciphertext:str):
        self.base=self.org #reset the base set
        self.fib(len(ciphertext)) # get the fib seuqence values
        new=""
        for i,s in enumerate(ciphertext):
            new+=chr((ord(s)//self.base[i])) #simple reverse transformation
        return new


new=Fib(13, 2) #the key is 13 and 2
cipher=new.cipher("Hello World")
decipher=new.decipher(cipher)

print(f'''The ciphered text is {cipher}
The deciphered text is {decipher}''')
