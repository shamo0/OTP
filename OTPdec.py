#!/usr/bin/env python3
#--------------------------------------------
#Author: Genadi Shamugia
#Program: OPTdec.py
#Description: Program implemets the decryption algorithm
#------------------------------------------------------------

import sys
import os

def main():
   
    fdKey=open(sys.argv[1],'rb')
    key=fdKey.read()

    fdCiph=open(sys.argv[2],'rb')
    Ciph = fdCiph.read()

    dec = decrypt(Ciph,key)
    
    fdDec=open(sys.argv[3],"w")
    fdDec.write(dec)

    fdCiph.close()
    fdKey.close()
    fdDec.close()
    return 


def decrypt(cipher,key):
    string =""
    for i in range(len(cipher)):
        string += chr(cipher[i] ^ key[i])

    return string

if __name__=="__main__":
    main()
