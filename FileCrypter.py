'''
Author:Bruno Soares Galdino
Description: A simple program that encrypt/decrypt files
Date:25/12/2016
Update:27/09/2017

'''

import string
import sys
import time
import os.path

def encrypt( src, len ):
    
    if len > 52 or len < 1:
        return
   
    if not os.path.exists( src ):
        print 'file not found'
        return
    
    file = open( src , 'r' )	
    
    out = open( 'encrypted.txt' , 'w' )
    
    alfa = string.ascii_letters
    
    beta = alfa[ len: ]+alfa[ 0 : len ]
    
    beta = beta[ : : -1 ]
    
    tab = string.maketrans( alfa , beta )
    
    
    out.write( string.translate( file.read( ) , tab ) )
    
    file.close( )
    
    out.close( )
    
    print 'output on encrypted.txt'

def decrypt( src , len ):
    
    if len > 20  or len < 1:
        return
    
    if not os.path.exists(src):
       print 'file not found'
       return
    
    file = open(src,'r')
    
    out = open('decrypted.txt','w')
    
    alfa = string.ascii_letters
    
    beta = alfa[len:]+alfa[0:len]
    
    beta = beta[::-1]
    
    tab = string.maketrans(beta,alfa)
    
    out.write(string.translate(file.read(),tab))
    
    file.close()
    
    out.close()
    
    print 'output on decrypted.txt'
	
print 'File cryptor'

while 1:
    
    option = raw_input('what to do ?:')
    
    if option == 'decrypt':
        decrypt(raw_input('source:'),input('int len:'))
    
    elif option =='encrypt':
        encrypt(raw_input("source:"),input('int len:'))

    elif  option == 'exit':
        sys.exit()

    elif option == 'help':
        print ' type <decrypt> to decrypt a file \n type <encrypt> to encrypt a file \n type <exit> to exit'
    
    else: print'command not found! type help'