### Password Manager
If you use the Internet much, you have a hundred different passwords for things like email accounts, subscriptions, banking, social media, and the like. The best passwords are long and complex (combining letters, numbers, symbols, and punctuation) and never reused across different accounts. With so many to remember, some people use a password manager to securely store everything behind a single, memorable master password of suitable complexity. Password managers make it easy to use strong passwords for every account - but they also introduce a single point of failure. Much has been said on both sides of the argument and the decision to use a password manager should be made carefully.

So, this is a light weight application used to save login credentials from any website.

------------
### Implementation
##### Account data

- All account data is stored in a SQL database with seperate records for each user.
- That file is encrypted using the Advanced Encryption Standard (AES) in Cipher-Block Chaining mode (CBC) mode.
- The file name is derived from the master user name and password by hashing with SHA-512.
- The encryption key is derived from the master password, the domain name, and a random salt via the PBKDF2 algorithm configured for SHA-512 and 1000 iterations.

------------
### To-Do:
- Add ability to import data from other password managers
- Convert to the Web Cryptography API (once widely available)
