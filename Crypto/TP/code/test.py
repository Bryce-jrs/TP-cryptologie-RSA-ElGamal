from common import * 


# test PGCD 

assert pgcd_iter(10,3) == 1
assert pgcd_iter(20,2) == 2
assert pgcd_iter(1,30) == 1

assert pgcd_rec(20,3)  == 1
assert pgcd_rec(15,3)  == 3
assert pgcd_rec(2,1)   == 1

# test algorithme d'euclide étendu 

assert euclide_ext(135,101) == (3,-4)
assert euclide_ext(120,23)  == (-9,47)
assert euclide_ext(141,255) == (38,-21)

# test inverse modulaire 

assert inverse_modulaire(17,4) == 13
assert inverse_modulaire(11,3) == 4
assert inverse_modulaire(14,3) == 5

# test expo_modulaire 

assert expo_modulaire(3,5,13) == 8
assert expo_modulaire(13,11,19) == 11
assert expo_modulaire(13,4,497) == 445

# test expo_modulaire rapide 

assert expo_modulaire_fast(3,5,13) == 8
assert expo_modulaire_fast(13,11,19) == 11
assert expo_modulaire_fast(13,4,497) == 445


# test crible d'Ératosthène 

assert crible_eras(2)  == [2]
assert crible_eras(9)  == [2,3,5,7]
assert crible_eras(17) == [2,3,5,7,11,13,17]

# test de fermat 

assert test_fermat(6,10) == False 
assert test_fermat(9576890767,1000) == True
assert test_fermat(95647806479275528135733781266203904794419563064407,3000) == True
assert test_fermat(100000000000000000000000000000000000000000000000,10) == False 

# test décomposition de rabin 

assert find_ru(10) == (1,5)
assert find_ru(7) == (0,7)


# test temoin de Rabin 

assert temoin_rabin(2,561)== True
assert temoin_rabin(3,261) == True
assert temoin_rabin(5,17) == False 

# test de Rabin

assert test_rabin(6,10) == False 
assert test_rabin(9576890767,1000) == True
assert test_rabin(95647806479275528135733781266203904794419563064407,3000) == True
assert test_rabin(100000000000000000000000000000000000000000000000,10) == False

# test generation de nombre premier

assert test_rabin(gen_prime(1000),100) == True
assert test_rabin(gen_prime(100),100) == True
assert test_rabin(gen_prime(10),100) == True

