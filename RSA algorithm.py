#27/10/2024 Silly little RSA (Rivest Shamir Adleman) encryptor
#do not actually use my implementation in practice, mine is light weight so I can actually run it on my PC (yet I still underestimated how resource intensive RSA is)

import random
import math

def highestCommonDivisor(a,b):
    while a%b!=0:
        a,b=b,a%b
    return(b)

def isCoprime(a,b):
    return(highestCommonDivisor(a,b)==1)

def selectExponent(n):
    values=[]
    for i in range(1,n):
        if isCoprime(i,n):
            values.append(i)
        if len(values)>5:
            break
    return(values[random.randint(1,len(values)-1)])

def splitBlocks(message,prod):
    prodLength,messageLength=len(message),len(str(prod))
    lastBlockSize=messageLength%(prodLength-1)
    numBlocks=prodLength//(prodLength-1)
    blocks=[]
    for i in range(numBlocks):
        blocks.append(message[i*(prodLength-1):(i+1)*(prodLength-1)])
    blocks.append(message[(numBlocks*(prodLength-1)):])
    return(blocks)

def generateLargePrimes(indexOne,indexTwo):
    n = 2000000
    sieve = [True]*n
    sieve[0]=sieve[1]=False
    for i in range(2,math.isqrt(n)):
        if sieve[i]==True:
            for j in range((i*i),n,i):
                sieve[j]=False
    primes=[]
    for i in range(len(sieve)):
        if sieve[i]:
            primes.append(i)
    chosenPrimes=[primes[indexOne],primes[indexTwo]]
    return(chosenPrimes)

def convertToASCII(text):
    number=""
    for i in range(len(text)):
        number+=str(ord(text[i]))
    return(number)


def encrypt(text,securityLevel):
    numberText=convertToASCII(text)
    if securityLevel=="low":
        primes=generateLargePrimes(random.randint(2,10), random.randint(2,10))
    elif securityLevel=="medium":
        primes=generateLargePrimes(random.randint(11,100000), random.randint(10,100000))
    else:
        primes=generateLargePrimes(random.randint(100000,148000), random.randint(100000,148000))
    primeOne,primeTwo=primes[0],primes[1]
    totient=(primeOne-1)*(primeTwo-1)
    prod=primeOne*primeTwo
    encryptionExponent=selectExponent(totient)
    print(encryptionExponent)
    print(totient)
    decryptionExponent=encryptionExponent**(totient-1)
    if int(numberText)>prod:
        blocks=splitBlocks(numberText,prod)
        encryptedBlocks=[]
        for i in range(len(blocks)):
            encryptedBlocks=str((int(blocks[i])**encryptionExponent)%prod)
        ciphertext=encryptedBlocks
    else:
        ciphertext=str((int(numberText)**encryptionExponent)%prod)

    return(f"encryption key (public): {[prod,encryptionExponent]}, decryption key (keep this one secret!): {[prod,decryptionExponent]}, ciphertext: {ciphertext}")

def decrypt(ciphertext,prod,exponent):
    plaintext=""
    if type(ciphertext)==list:
        for i in range(len(ciphertext)):
            plaintext+=chr((int(ciphertext[i])**exponent)%prod)
    else:
        plaintext=chr((int(ciphertext)**exponent)%prod)
    return(plaintext)


    

choice=input("Would you like to encrypt or decrypt a message? (encrypt/decrypt)")

if choice.lower()=="encrypt":
    plaintext=input("enter some text: ")
    securityLevel=input(("enter security level (low/medium/highest): "))
    print(encrypt(plaintext,securityLevel))

if choice.lower()=="decrypt":
    ciphertext=input("enter the ciphertext")
    prod=int(input("enter the first part of the key"))
    exp=int(input("enter the second part of the key"))
    print(decrypt(ciphertext,prod,exp))