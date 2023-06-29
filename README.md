# Cryptographic Algorithms: RSA and ElGamal

This repository provides an implementation and explanation of two widely used cryptographic algorithms: RSA and ElGamal. These algorithms are based on different mathematical principles and provide secure encryption and decryption methods for secure communication and data protection.

## RSA (Rivest-Shamir-Adleman)
RSA is an asymmetric encryption algorithm named after its inventors: Ron Rivest, Adi Shamir, and Leonard Adleman. It involves the use of a public key and a private key, and it is based on the mathematical properties of large prime numbers.

### Key Generation:
1. Select two distinct prime numbers, p and q.
2. Compute the modulus, n = p * q.
3. Calculate Euler's totient function, φ(n) = (p - 1) * (q - 1).
4. Choose a public exponent, e, such that 1 < e < φ(n) and gcd(e, φ(n)) = 1.
5. Compute the private exponent, d, as the modular multiplicative inverse of e modulo φ(n).

### Encryption:
1. Convert the plaintext message to a numeric representation.
2. Use the recipient's public key (n, e) to encrypt the message using modular exponentiation: ciphertext = plaintext^e mod n.

### Decryption:
1. Use the recipient's private key (n, d) to decrypt the ciphertext using modular exponentiation: plaintext = ciphertext^d mod n.

## ElGamal
ElGamal is an asymmetric encryption algorithm developed by Taher ElGamal. It also involves the use of a public key and a private key, and it is based on the mathematical properties of discrete logarithms.

### Key Generation:
1. Select a large prime number, p, and a primitive root, g, modulo p.
2. Choose a random integer, x, such that 1 < x < p-1.
3. Compute the public key as y = g^x mod p.
4. The public key consists of the values (p, g, y), while the private key is x.

### Encryption:
1. Convert the plaintext message to a numeric representation.
2. Choose a random integer, k, such that 1 < k < p-1 and gcd(k, p-1) = 1.
3. Compute the ciphertext as a pair of values: (c1, c2), where c1 = g^k mod p and c2 = (plaintext * y^k) mod p.

### Decryption:
1. Retrieve the ciphertext values (c1, c2).
2. Compute the shared secret as s = c1^x mod p.
3. Compute the modular inverse of s modulo p: s_inv = s^(-1) mod p.
4. Retrieve the plaintext message as plaintext = (c2 * s_inv) mod p.

These algorithms offer secure encryption and decryption methods, ensuring confidentiality and integrity in communication. The security of RSA relies on the difficulty of factoring large numbers, while ElGamal's security is based on the computational difficulty of the discrete logarithm problem.
