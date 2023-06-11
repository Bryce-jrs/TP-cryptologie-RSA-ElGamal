import random
import sys
from math import sqrt


####################
# Q1
####################

# retourne le pgcd de deux entiers naturels
def pgcd_iter(a,b):
    """ Returns pgcd of a and b iteratively """
    while b != 0:
        tmp = b
        b = a % b
        a = tmp
    return a

def pgcd_rec(a,b):
    """ Returns pgcd of a and b recursively """
    if b == 0:
        return a
    else:
        return pgcd_rec(b, a % b)
    

# algo euclide etendu
# retourne d,u,v avec pgcd(a,b)=d=ua+vb
def euclide_ext(a,b):
    """ Extended euclide """
    if b == 0:
        return (1, 0)
    else:
        (u, v) = euclide_ext(b, a % b)
        return (v, u - (a // b) * v)
    
####################
# Q2
####################

# retourne un entier b dans [1,N-1] avec ab=1 modulo N
def inverse_modulaire(N,a):
    """ Modular inverse """
    (u,v) = euclide_ext(a,N)
    if(u<0):
        u = u + N
    return u

####################
# Q3
####################

# retourne (b**e) % n
# calcule le modulo apres chaque multiplication
def expo_modulaire(e,b,n):
    """ Modular exponentation """
    if n == 1:
        return 0
        
    if e == 0:
        return 1

    res = 1
    while e > 0:
        res = (res * b) % n
        e = e - 1
    return res

####################
# Q4
####################

# retourne (b**e) % n
# calcule le modulo apres chaque multiplication
# O(log(e)) operations
def expo_modulaire_fast(e,b,n):
    # help:
    
    # representer e en binaire
    #bin_e = bin(e)[2:]
    
    # utile pour iterer sur chaque element de e 
    #for x in range(len(bin_e)):
    #   int(bin_e[x])
    """ Rapid modular exponentiation """
    if n == 1:
        return 0
    p = 1
    count = 0
    for bit in format(e, 'b'):
        count += 1
        p = (p * p ) % n
        if bit == '1':
            p = (p * b) % n
            count += 1
    return p

####################
# Q5
####################

# retourne la liste des nombres premiers <= n
# methode du crible d Eratosthene
def crible_eras(n):
    P = [ ]
    for i in range(2,n+1):
        if len(P) == 0:
            P.append(i)
        else:
            prem = True
            for k in P:
                if i % k == 0:
                    prem = False
            if prem == True:
                P.append(i)
    return P
        
####################
# Q6
####################

# input: n  
# input: t number of tests
# test if prime according to fermat
# output: bool if prime 
def test_fermat(n,t):
    # random number generator between a and b
    #x = random.randint(a,b)
    """ Fermat  primality test"""
    if t > n-1 :
        t = n-1
    for i in range(1,t):
        a = random.randint(1,n-1)
        if(expo_modulaire_fast(n-1,a,n) != 1):
            return False
    return True

####################
# Q7
####################

# input: n
# output: r and u coefficient
# for rabin test 
# returns r,u such that 2^r * u = n and u is odd
def find_ru(n):
    """ Rabin decomposition """
    r = 0
    tmp = n
    while tmp % 2 == 0:
        tmp = tmp // 2
        r = r + 1
    u = n // (pow(2,r))
    return (r, u) 

####################
# Q8
####################

#n entier
#a entier dans [1,n-2]
#pgcd(a,n)=1
#retourne True , si a est un temoin de Rabin de non-primalite de n
def temoin_rabin(a,n):
    # utilisez expo_modulaire_fast !
    """ Rabin proof """
    r,u = find_ru(n - 1)
    m = expo_modulaire_fast(u, a, n)
    if m == 1 or m == n - 1:
        return False
    for i in range(1, r):
        if expo_modulaire_fast(u * pow(2,i), a, n) == n - 1:
            return False
    return True


#n entier a tester, t nombre de tests
#retourne True , si n est premier
#retourne False , avec proba > 1-(1/4)**t, si n est compose
def test_rabin(n,t):
    """ Rabin primality test """
    if n == 2:
        return True
    if n % 2 == 0 or n == 1:
        return False
    for i in range(t):
        a = random.randint(1, n - 1)
        if pgcd_iter(a, n) != 1:
            return False
        if temoin_rabin(a, n):
            return False
    return True 
            
# prime generator
# output: n range for prime number
# utilise votre implementation de rabin (ou la plus effice si rabin non dispo)
# pour generer un nombre premier sur n bits.
# range de n: p = random.randint(pow(2,n-1),pow(2,n)-1)
def gen_prime(n):
    """ Generates prime number """
    x = random.randint(pow(2,n-1),pow(2,n)-1)
    if test_fermat(x,1000):
        if test_rabin(x,1000):
            return x
        else:
            return gen_prime(n)
    else:
        return gen_prime(n)

####################
# Helper functions for rsa/elgamal
####################

# Helper function
# convert str to int
def str_to_int(m):
    s = 0
    b = 1
    for i in range(len(m)):
        s = s + ord(m[i])*b
        b = b * 256
    return s

# Helper function
# convert int to str
def int_to_str(c):
    s = ""
    q,r = divmod(c,256)
    s = s+str(chr(r))
    while q != 0:
        q,r = divmod(q,256)
        s = s+str(chr(r))
    return s
