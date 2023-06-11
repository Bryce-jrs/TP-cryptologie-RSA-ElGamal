from elgamal import *
from common import * 


# test gen_elgamal_pg 

(p,g) = gen_elgamal_pg(64)
print(p)
print(g)
assert test_rabin(p,1000)== True

# test  gen_elgamal_sk_pk

[s_ka,p_ka] = gen_elgamal_sk_pk(p,g)
[s_kb,p_kb] = gen_elgamal_sk_pk(p,g)
print([s_ka,p_ka])
print([s_kb,p_kb])

# test gen_elgamal_get_secret

secret_key = gen_elgamal_get_secret(s_ka,p_ka,s_kb,p_kb,p)
print("secret key: ",secret_key)

# test encodage elgamal

m = 'test1'
cipher_m = enc_elgamal(m,secret_key,p)
assert cipher_m != m


# test decodage 
plaintext = dec_elgamal(enc_elgamal(m,secret_key,p),secret_key,p)
assert plaintext == 'test1'


# test signature El Gamal

[r,s] = elgamalsignature(g,p,s_ka,m)
print([r,s])
assert elgamalverification(g,p,r,s,m,p_ka) == True