import string
import os,binascii
import random
import ecdsa
import codecs

def generate_key():

    input1 =input("generate private key automatically? (y/n)")
    if input1 != 'y':
        private_key = input("enter private key")
    else:
        private_key = binascii.b2a_hex(os.urandom(540))
    print(private_key)

    public_key = ecdsa.SigningKey.from_string(private_key.decode('hex'), curve=ecdsa.SECP256k1).verifying_key
    print (public_key)
generate_key()