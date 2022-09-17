# cryptography
Some new cryptographic algorithms based on the bitwise operator xor.

## Pairwise- and chaining xoring

If we have a data sequence like including numbers or chars, we can apply bitwise xor operator on it pairwise and chainly.

The pairwise xoring on an S sequence: T : s_1, s_2, s_3, s_4, ... -> 0 (+) s_1, s_1 (+) s_2, s_2 (+) s_3, s_3 (+) s_4, ...

The chaining xoring on an S sequence: T' : s_1, s_2, s_3, s_4, ... -> 0, s_1, s_1 (+) s_2, s_1 (+) s_2 (+) s_3, ...

Theory 1.: The pairwise xoring is the inverse of the chaining xoring. In other words: the pairwise xoring of the chaining xored S sequence is S itself, or equevalently: the chaining xoring of pairwise xored S sequence is S itself. With formula: T o T' o S = T' o T o S = S.

Let us have a famouse quote from Friedrich Nietzsche as a plain text, and encrypt it with our xoring methods:

plain = "GOD_IS_DEAD"

print(xor_chain(plain))

\# GIN^W[M^HED

print(xor_pairwise(plain))

\# GILV^PRSWWV

Both of xor_pairwise(xor_chain(plain)) and xor_chain(xor_pairwise(plain)) returns with the original plain text.

So our encryption and decryption algorithms are working.

## Xorterian Hash

During xorterian hashing we apply the pairwise xoring.

If we want to get a 64-long-hash from a plain text like previous, we get one really differs from hashes of a similar but tiny changing plain texts:

print(hash('GOD_IS_DEAD'))

\# [MYPDaBhnJrGuujEmvowgbsywsfpculmDDGNAHGOJPLT\`VHOYREXKUU]GCFGFFDN

print(hash('G0D_IS_DEAD'))

\# HL][GNHYQOwitaWCTJAqcghDwrupZxSXHEAJEAAKMWTX[M\`K^I]OyNgFu\x\`x][o

print(hash('GOD_IS_DAD'))

\# V\`W\[^DoBieAKBPKCSBXPREGUD\`XD[FTPEFQMED_P[LMRZLP\RGSNLKPOIIGLYDK

This algorithm satisfies the wish that for even tiny changes the hash hops a big.

The distadvantage of the algorithms is the easy-to-crackness if you own the source code. Let me show some ways to make it harder.

## Complexity

The whole encryption-decryption and hashing are based on the duality of bitwise xoring. In a nutshell:

A (+) 0 = A

A (+) A = 0

A (+) B != 0 eq A != B

My first comment is that in the pairwise xoring method you can make the xoring parallel, while in the chaining method you have to wait for the result of the last subchain xoring. So if the complexity of the operator xoring is O(n) for elements measured in n-s of byte and the length of the sequence is m, then the complexity of pairwise xoring is O(m×n), and the complexity of chaining xoring is O(m^2×n).

My second comment is that you can figure non-dual xoring out like trial and quadral ones, in general:

A (+)_n 0 = A

A (+)_n ... (+)_n A = 0 (n-times)

E.g.

A (+)_3 A (+)_3 A = 0

like tritwise xoring.

Attention! With too big n, it is too similar to raw addition.

If we have elements represented with enough big n bits, a non-trivial alpha arity of xoring but satisfying 2 << alpha << n, and enough long S sequence, |S| = m, then 
by applying 3-wise, 4-wise,... xoring comes with its inverse, 3-ple, 4-ple,... chaining methods instead of pairwise, you get a lot of setup variables to fine-tune the the correct range in which it is impossible the crack your encryptions and hashes under a complexity.
