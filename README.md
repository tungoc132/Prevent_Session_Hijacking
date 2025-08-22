# Prevent Session Hijacking By One-time Cookies
Stolen HTTPP cookies, which are commonly used to identify users and maintain authenticated sessions, can allow attackers to hijack active sessions and impersonate legitimate users. The following solution strengthens session security by combining ephemeral cookie tokens with encrypted session data, reducing the attack surface for session hijacking.

## To mitigate this risk, the project implements:
- ```One-Time Cookies``` – ensuring cookies cannot be reused after a single valid session or request, reducing exposure to replay and hijacking attacks.
- ```Cookie Encryption``` – sensitive data within cookies is encrypted to maintain confidentiality and integrity, preventing unauthorized access or tampering.

## Setup & Installtion
Make sure you have the latest version of Python installed.
```bash
git clone <repo-url>
pip install -r requirements.txt
```
Run the app
```bash
python main.py
```
View the app - Go to `http://127.0.0.1:5000`
