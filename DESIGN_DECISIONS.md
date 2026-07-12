## Password Hash Storage
Modern password hashes (bcrypt, Argon2) are self-describing.
The hashing library detects the algorithm from the stored hash and supports automatic migration to newer algorithms.

If I ever have to switch from bcrypt to argon2 then Passlib supports rehashing(Automatic Hash Migration) through its:
Passlib CryptContext.verify_and_update()