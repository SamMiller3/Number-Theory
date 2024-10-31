# 31/10/2024 Silly little RSA (Rivest Shamir Adleman) encryptor
# do not actually use my implementation in practice, mine is light weight so I can actually run it on your pc without crashing

import random
import math

def highest_common_divisor(a,b):
    
    # calculate HCD using Euclidean algorithm

    while a%b!=0:
        a,b=b,a%b
    return(b)

def is_coprime(a,b):

    # if HCD is 1 then a%b are coprime

    return(highest_common_divisor(a,b)==1)

def select_exponent(n):

    # exponent is selected by finding first 5 coprimes then selecting a random value from this list and returning it

    values=[]
    for i in range(1,n):
        if is_coprime(i,n):
            values.append(i)
        if len(values)>5:
            break
    return(values[random.randint(1,len(values)-1)])

def split_blocks(message,product):
    product_length = len(str(product))
    blocks = []
    max_block=product_length-1

    # Continue until the message is empty

    while message > 0:

        # Get the maximum block size that fits within the allowed value

        block = message % (10 ** (max_block))  # Keep only the last digits that fit
        blocks.append(block)
        message //= (10 ** (max_block))  # Reduce the message by removing the block size digits

    blocks.reverse()  # Reverse to maintain the order
    return blocks

def generate_large_primes(index_one,index_two):

    n = 2000000 # generate primes up to 2 million using Sieve of Eratosthenes
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

    chosen_primes=[primes[index_one],primes[index_two]]
    return(chosen_primes)

def convert_to_ASCII(text):
    number = ""
    for char in text:
        number += f"{ord(char):03}"  # Pads each ASCII code to 3 digits
    return int(number)


def encrypt(text,security_level):

    number_text=convert_to_ASCII(text) # convert text to ascii and pad each character to be 3 digits

    if security_level=="low": # generate primes to the size corresponding with the security level
        primes=generate_large_primes(random.randint(2,10), random.randint(2,10))
    elif security_level=="medium":
        primes=generate_large_primes(random.randint(11,100000), random.randint(10,100000))
    else:
        primes=generate_large_primes(random.randint(100000,148000), random.randint(100000,148000))
    
    prime_one,prime_two=primes[0],primes[1] # generate large primes
    totient=(prime_one-1)*(prime_two-1) # calculate totient
    product=prime_one*prime_two 
    encryption_exponent=select_exponent(totient) #choose an exponent that is coprime but less than totient
    decryption_exponent = pow(encryption_exponent, -1, totient) # find Modular multiplicative inverse

    if int(number_text)>product:
        # Split into blocks if the number exceeds the productuct
        blocks = split_blocks(number_text, product)
        ciphertext_blocks = [str(pow(block, encryption_exponent, product)) for block in blocks] # encrypt each block
        ciphertext = ','.join(ciphertext_blocks)  # Join blocks into a single string

    else:
        ciphertext=str(pow(number_text,encryption_exponent,product)) # encrypt

    return(f"encryption key (public): {[product,encryption_exponent]}, decryption key (keep this one secret!): {[product,decryption_exponent]}, ciphertext: {ciphertext}")


def decrypt(ciphertext,product,exponent):
    plaintext = ""
    
    # Split the ciphertext string into individual blocks
    ciphertext_blocks = ciphertext.split(',')
    
    for block in ciphertext_blocks:
        # Decrypt each block
        numberText = str(pow(int(block), exponent, product))

        # Ensure the numberText is properly padded to the right length
        # Concatenate the decrypted blocks
        plaintext += numberText.zfill(len(block) * 3)  # Pad with zeros if necessary

    # Now convert the complete numeric string back to the original text
    original_text = ""
    for i in range(0, len(plaintext), 3):
        original_text += chr(int(plaintext[i:i+3]))
        
    return original_text


choice=""
while choice!="exit":
    choice=input("Would you like to encrypt or decrypt a message? (encrypt/decrypt/exit)")

    if choice.lower()=="encrypt":
        plaintext=input("enter some text: ")
        security_level=input(("enter security level (low/medium/highest): "))
        print(encrypt(plaintext,security_level))

    if choice.lower()=="decrypt":
        ciphertext=input("enter the ciphertext")
        product=int(input("enter the first part of the key"))
        exp=int(input("enter the second part of the key"))
        print(decrypt(ciphertext,product,exp))
