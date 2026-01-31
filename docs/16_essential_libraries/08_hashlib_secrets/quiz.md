# 🔐 Hashlib & Secrets - Quiz

Test your knowledge of hashing and secure random generation!

---

## Question 1
**What is the main difference between hashing and encryption?**

A) Hashing is faster
B) Hashing is one-way, encryption is two-way
C) Encryption requires a password
D) There is no difference

<details>
<summary>Click for answer</summary>

**B) Hashing is one-way, encryption is two-way**

You can decrypt encrypted data, but you cannot "unhash" a hash.
</details>

---

## Question 2
**Which hash algorithm should you use for cryptographic purposes?**

A) MD5
B) SHA1
C) SHA-256
D) CRC32

<details>
<summary>Click for answer</summary>

**C) SHA-256**

MD5 and SHA1 are cryptographically broken. CRC32 is not a cryptographic hash.
</details>

---

## Question 3
**Why should you use `secrets` instead of `random` for security?**

A) `secrets` is faster
B) `random` is not cryptographically secure
C) `secrets` has more features
D) `random` is deprecated

<details>
<summary>Click for answer</summary>

**B) `random` is not cryptographically secure**

`random` is predictable; `secrets` uses OS-provided cryptographically secure random.
</details>

---

## Question 4
**What is a salt in password hashing?**

A) Extra characters added to the password
B) Random data added before hashing to prevent rainbow table attacks
C) A type of encryption
D) A secret key

<details>
<summary>Click for answer</summary>

**B) Random data added before hashing to prevent rainbow table attacks**

Each password gets a unique salt, making precomputed hash tables useless.
</details>

---

## Question 5
**What does `secrets.compare_digest()` do?**

A) Compares two strings
B) Compares strings in constant time to prevent timing attacks
C) Checks if a digest is valid
D) Creates a digest

<details>
<summary>Click for answer</summary>

**B) Compares strings in constant time to prevent timing attacks**

Regular string comparison takes different time based on how many characters match.
</details>

---

## Question 6
**What is `secrets.token_urlsafe()` used for?**

A) Creating passwords
B) Generating secure tokens for URLs
C) Encrypting URLs
D) Hashing URLs

<details>
<summary>Click for answer</summary>

**B) Generating secure tokens for URLs**

Generates random text safe for use in URLs (no problematic characters).
</details>

---

## Question 7
**Why shouldn't you use SHA-256 alone for password hashing?**

A) It's too slow
B) It's too fast, making brute force attacks easier
C) It produces too short output
D) It's broken

<details>
<summary>Click for answer</summary>

**B) It's too fast, making brute force attacks easier**

Password hashing should be slow. Use bcrypt, argon2, or scrypt instead.
</details>

---

## Question 8
**What is the output size of SHA-256?**

A) 128 bits
B) 256 bits (32 bytes / 64 hex characters)
C) 512 bits
D) Variable

<details>
<summary>Click for answer</summary>

**B) 256 bits (32 bytes / 64 hex characters)**

SHA-256 produces a 256-bit (32-byte) hash, represented as 64 hex characters.
</details>

---

## Question 9
**How do you hash a large file efficiently?**

A) Read entire file and hash
B) Read in chunks and update hash
C) Use a different algorithm
D) Compress first

<details>
<summary>Click for answer</summary>

**B) Read in chunks and update hash**

Use `hash.update()` repeatedly with chunks to avoid loading large files into memory.
</details>

---

## Question 10
**What is the recommended minimum length for a secure random token?**

A) 8 bytes
B) 16 bytes (32 hex chars / ~22 URL-safe chars)
C) 4 bytes
D) 64 bytes

<details>
<summary>Click for answer</summary>

**B) 16 bytes (32 hex chars / ~22 URL-safe chars)**

16 bytes (128 bits) provides sufficient entropy for most security purposes.
</details>

---

**How did you do?** Check `examples.py` for more practice!
