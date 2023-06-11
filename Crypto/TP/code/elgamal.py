import random
import sys
from math import sqrt
from common import *

####################
# Q14
####################

# retourne p g 
# g generateur sur le groupe Z*p => on utilise 3
# p premier sur n bits.
def gen_elgamal_pg(n):
    p = gen_prime(n)
    g = 3
    return (p,g)
    
####################
# Q15
####################

# retourne couple cle prive/publique [sk,pk]
# definit tel que sk compris entre (3,p-2) 
# pk =  g^sk [p]
# output: [sk,pk]
def gen_elgamal_sk_pk(p,g):
    s_k = random.randint(3,p-2)
    p_k = expo_modulaire_fast(s_k,g,p)
    return [s_k,p_k]

####################
# Q16
####################
    
# pk_a,sk_a,pk_b,sk_b sont les cles publiques prive de A B modulo p
# retourne le secret partage par A et B
def gen_elgamal_get_secret(pk_a,sk_a,pk_b,sk_b,p):
    share_secret1 = expo_modulaire_fast(pk_a,sk_b,p)
    share_secret2 = expo_modulaire_fast(pk_b,sk_a,p)
    assert share_secret1 == share_secret2
    return share_secret1

####################
# Q17
####################

# chiffrement du message m avec le secret
# output: chaine de caractere c en binaire represantant c 
# contrainte: secret plus grand que message 
def enc_elgamal(m,secret,p):
    int_m = str_to_int(m)
    c = (int_m*secret)%p
    str_c = int_to_str(c)
    return str_c


# dechiffrement du message c avec le secret
# output: chaine de charactere m 
# contrainte: secret plus grand que message
def dec_elgamal(c,secret,p):        
    int_c = str_to_int(c)
    m = (int_c*inverse_modulaire(p,secret))%p
    str_m =  int_to_str(m)
    return str_m

####################
# Q19
####################
 
# retourne la signatue [r, s]
# sk cle secrete utilise pour signer message m
# m sous forme de texte     
def elgamalsignature(g,p,sk,m):
    k = random.randint(3,p-2)
    while pgcd_iter(k,p-1) != 1:
        k = random.randint(3,p-2)
    r = expo_modulaire_fast(k,g,p)
    int_m = str_to_int(m)
    s = ((int_m - r*sk) * inverse_modulaire(p-1,k))%(p-1)
    return [r,s]
    
# r,s signature
# pk cle publique utilise pour signer message m
# m sous forme de texte 
# output: bool verifie si signature valide
# true = valid  
def elgamalverification(g,p,r,s,m,pk):
    int_m = str_to_int(m)
    test = (expo_modulaire_fast(int_m,g,p) - expo_modulaire_fast(r,pk,p) * expo_modulaire_fast(s,r,p))%p
    if test == 0:
        return True
    return False
