# SHA 256 implemented from scratch including the bitwise operations, functions and bitwise addition in binary
# 22/06/2025 

def right_rotate(A,n): # insert last element into first element and pop last element n times
    for i in range(n):
        A=A[-1]+A
        A=A[:-1]
    return(A)

def shift_right(A,n): # insert first element as 0 and remove last element n times
    for i in range(n):
        A="0"+A
        A=A[:-1]
    return(A)

def XOR(A,B): # perform bitwise XOR mask on A and B
    C=""
    for i in range(len(A)):
        if A[i]!=B[i]:
            C+="1"
        else:
            C+="0"
    return(C)

def AND(A,B): # perform bitwise AND mask on A and B
    C=""
    for i in range(len(A)):
        if A[i]==B[i] and A[i]=="1":
            C+="1"
        else:
            C+="0"
    return(C)

def OR(A,B): # perform bitwise OR mask on A and B
    C=""
    for i in range(len(A)):
        if A[i]=="1" or B[i]=="1":
            C+="1"
        else:
            C+="0"
    return(C)

def NOT(A): # perform bitwise NOT mask on A
    C=""
    for i in range(len(A)):
        if A[i]=="1":
            C+="0"
        if A[i]=="0":
            C+="1"
    return(C)

def choice(X,Y,Z): # if X is 1 then return Y if X is 0 return Z
    return(
        XOR( AND(X,Y), (AND(NOT(X), Z)) ) 
        )

def majority(X,Y,Z): # return the majority value at each bit index
    return(
        XOR( XOR( AND(X, Y), AND(X, Z))
        , AND(Y, Z))
    )

# big and small sigma functions

def Sigma0(X): 
    return(
        XOR( XOR(right_rotate(X,2), right_rotate(X,13)),right_rotate(X,22))
        )

def Sigma1(X):
    return(
        XOR( XOR(right_rotate(X,6), right_rotate(X,11)),right_rotate(X,25))
        )

def sigma0(X):
    return(
        XOR( XOR(right_rotate(X,7), right_rotate(X,18)),shift_right(X,3))
        )

def sigma1(X):
    return(
        XOR( XOR(right_rotate(X,17), right_rotate(X,19)),shift_right(X,10))
        )

# 32 bit binary addition

def binary_addition_mod_32(A,B):
    carry="0"
    result=""
    A,B=A[::-1],B[::-1] # reverse inputs so they can be processed in order
    for i in range(len(A)):
        if A[i]==B[i] and A[i]=="1": # 1 + 1
            if carry=="1":
                result+="1"
            else:
                result+="0"
            carry="1"
        elif A[i]!=B[i] and (A[i]=="1" or B[i]=="1"): # 1 + 0
            if carry=="1":
                result+="0"
            else:
                result+="1"
        else: # 0 + 0
            if carry=="1":
                result+="1"
                carry="0"
            else:
                result+="0"
    result=result[::-1]
    
    if len(result) > 32:
        return result[-32:]  # Take last 32 bits
    else:
        return result.zfill(32)  # Pad to 32 bits if shorter



K = [
   '01000010100010100010111110011000',
   '01110001001101110100010010010001',
   '10110101110000001111101111001111',
   '11101001101101011101101110100101',
   '00010000011010101010000001110000',
   '00100100001111110110101010001001',
   '01010101000011000111110100000011',
   '01110010101111100101110001010101',
   '10000000110111101011000111111110',
   '10011011110111000000011010100111',
   '11000001100110111111000101110100',
   '11010101101001111001000101000111',
   '00000110110010100110001101010001',
   '00010100001010010010100101100111',
   '00100111101101110000101010000001',
   '01001010011101001000010010101010',
   '01011100101100001010100111011100',
   '01110110111110011000100011011010',
   '10011000001111100101000101010010',
   '10101000001100011100011001101101',
   '10110000000000110010011111001000',
   '10111111010010010110010101100001',
   '11000110111000000000001011101111',
   '11010100111010010110000110110011',
   '00001111000000011010110111000101',
   '00100001111111000101001110110000',
   '00101011111110011100101010010010',
   '01110100111110011111010000000110',
   '10011101101001000000111000010010',
   '10111110101111011110011010100101',
   '11001100000100000110010100100111',
   '11101011101101111111110001000100',
   '00000100110110001110010110110001',
   '00010110101001000000101110100110',
   '01000111101101100100011001001010',
   '01011011110111100000111100111000',
   '01101000110100001100110001011010',
   '01110110011010000000010000100000',
   '10001001101001111000110010111001',
   '10010111110101101110000000100001',
   '10110111110001000001000101111010',
   '11000100111100100001010001010100',
   '11010110110010100100010010100000',
   '11100010110000000101001101011100',
   '11110110000000001101001110110100',
   '00001000110100001001000001100000',
   '00011101100100010010001100010101',
   '00100010010110001000010110010001',
   '00101100110001011100010110001010',
   '01010010000101001111101000110100',
   '01011100100100111100100001110011',
   '01110110010110000010000101000001',
   '10000010110000111000110011001001',
   '10010100011110010000010010111101',
   '10110001001111100001110000000001',
   '11000000101100000001110000001010',
   '11001100000110001001010000101010',
   '11101100000000010100001100100101',
   '11111000000001001000110110101001',
   '00000100110001111011010110001101',
   '00100011010100000100001100100001',
   '00101111100111101001110110111010',
   '01101100100101101110001010001100',
   '10001101010011101001000110100110'
]

H = [
    '01101010000010011110011001100111',  # H0
    '10111011011001111010111010000101',  # H1
    '00111100011011101111001101110010',  # H2
    '10100101010011111111010100111010',  # H3
    '01010001000011100101001001111111',  # H4
    '10011011000001010110100010001100',  # H5
    '00011111100000111101100110101011',  # H6
    '01011011111000001100110100011001'   # H7
]

message = input("enter an input: ")
preprocessed_message = "".join(format(ord(i), "08b") for i in message) # convert message to binary

preprocessed_message+="1" # preprocess/pad message
zeros_needed = (448 - len(preprocessed_message)) % 512 
preprocessed_message+="0"*zeros_needed
preprocessed_message+=format(len(message)*8, "064b")
hash_message=""

for i in range(0,len(preprocessed_message),512): 

    words = [preprocessed_message[j : j + 32] for j in range(i, i + 512, 32)] # block decomposition
    for j in range(16, 64):
        w_minus_16 = words[j-16]
        w_minus_15 = words[j-15] 
        w_minus_7 = words[j-7]
        w_minus_2 = words[j-2]
        
        sigma0_result = sigma0(w_minus_15)
        sigma1_result = sigma1(w_minus_2)
        
        words.append(binary_addition_mod_32(binary_addition_mod_32 (binary_addition_mod_32(w_minus_16, sigma0_result), w_minus_7),
        sigma1_result))
    

    a,b,c,d,e,f,g,h=H[0],H[1],H[2],H[3],H[4],H[5],H[6],H[7] # Hash computation
    for t in range(64):
        T1 = binary_addition_mod_32(
            binary_addition_mod_32( 
            binary_addition_mod_32(
            binary_addition_mod_32( h, Sigma1(e) )
            ,choice(e,f,g)),
            K[t]),
            words[t])

        T2 = binary_addition_mod_32(Sigma0(a), majority(a,b,c))
        h=g
        g=f
        f=e
        e=binary_addition_mod_32(d,T1)
        d=c
        c=b
        b=a
        a=binary_addition_mod_32(T1,T2)
    H[0] = binary_addition_mod_32(H[0], a)
    H[1] = binary_addition_mod_32(H[1], b)
    H[2] = binary_addition_mod_32(H[2], c)
    H[3] = binary_addition_mod_32(H[3], d)
    H[4] = binary_addition_mod_32(H[4], e)
    H[5] = binary_addition_mod_32(H[5], f)
    H[6] = binary_addition_mod_32(H[6], g)
    H[7] = binary_addition_mod_32(H[7], h)
hash_message=H[0]+H[1]+H[2]+H[3]+H[4]+H[5]+H[6]+H[7] # concatenate hash values
hash_message = hex(int(hash_message, 2))[2:].zfill(64) # convert to hex
print(hash_message)