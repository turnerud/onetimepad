# onetimepad
Python

Encryption() takes a couple plaintexts, takes the binary of this plaintext, takes a randomly-generated binary key, and combines them using XOR to give a ciphertext.

Decryption() assumes one has the plaintext of one text (let's say P1), and the ciphertext to that text (let's say C1), as well as the ciphertext of another text (let's say C2). By reverse engineering the plaintext from the XOR of the ciphertext and key, one can decode C2 into plaintext.
