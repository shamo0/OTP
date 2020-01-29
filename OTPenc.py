#!/usr/bin/env python3
#--------------------------------------------
#Author: Genadi Shamugia
#Program: OPTenc.py
#Description: Program implemets the encryption algorithm
#------------------------------------------------------------

import sys
import os

def main():
   
    fdKey=open(sys.argv[1],'rb')
    key=fdKey.read()

    fdMsg=open(sys.argv[2],'rb')
    message = fdMsg.read()

    ciph = encrypt(message,key)
    
    fdCiph=open(sys.argv[3],"wb")
    fdCiph.write(ciph)

    fdCiph.close()
    fdKey.close()
    fdMsg.close()
    return 


def encrypt(M,key):
    #M=msg.encode()
    c= bytearray(len(M))
    for i in range(len(M)):
        c[i] = key[i] ^ M[i]
    print(c)
    return c

if __name__=="__main__":
    main()
