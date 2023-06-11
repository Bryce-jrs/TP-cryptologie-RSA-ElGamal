import random
import sys
from math import sqrt
from common import *

####################
# Q9
####################

# générer un nombre premier avec n 
def phi_prime(n):
    """ Generates prime number with phi """
    while True:
        num = random.randint(2, n)
        if pgcd_iter(num, n) == 1:
            return num

# input: n
# output: e,d,N
def gen_rsa(l):
    """ Generates key couple pk = n,e and sk = d """
    p, q = 0, 0
    
    while q == p :
        p = gen_prime(l//2)
        q = gen_prime(l - l // 2)

    n = p * q
    phi = (p - 1) * (q - 1)
    
    e = phi_prime(phi)
    
    d = inverse_modulaire(e,phi)
    if d < 0 :
        d = d % phi
    
    return (n,e,d)
    
####################
# Q10
####################    
    
# e exponent
# N modulo
# m message
# output: c
# message/cipher sous forme de nombre
def enc_rsa(m,e,N):
    """ Encrypts message m using pk = n, e """
    return expo_modulaire_fast(e, m, N)

# d exponent
# N modulo
# c cipher 
# output m   
# message/cipher sous forme de nombre
def dec_rsa(c,d,N):
    """ Encrypts message c using sk = d, n """
    return expo_modulaire_fast(d, c, N)

####################
# Q11
####################

# e exponent
# N modulo
# m message sous forme de texte
# output: c sous forme de nombre
def RSAcipher(e,N,m):
    return 0
    # utilisez str_to_int

# d exponent
# N modulo
# c cipher sous forme de nombre
# output: m message sous forme de texte
def RSAdecipher(d,N,c):
    return 0
    # utilisez int_to_str


####################
# Q13
####################

# d exponent
# N modulo
# m message sous forme de texte
# output: sig
def RSAsignature(d,N,m):
    return 0

# e exponent
# N modulo
# m message sous forme de texte
# sig signature
# output: bool verifie si signature valide
# true = valid
def RSAverification(e,N,m,sig):
    return 0