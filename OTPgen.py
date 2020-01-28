#!/usr/bin/env python3
#--------------------------------------------
#Author: Genadi Shamugia
#Program: OPTgen.py
#Description: Program implemets the key generation algorithm
#------------------------------------------------------------

import sys
import os

def main():
    
    keySize = int(sys.argv[1])
    k=os.urandom(keySize)
    print(k)

    fd=open(sys.argv[2],'wb')
    fd.write(k)
    fd.close()
    return


if __name__=="__main__":
    main()

